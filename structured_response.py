from typing import TypeVar

from typing import Type
from pydantic import BaseModel
from system_prompt import system_prompt

from model import llm
import convert_llama_ggml_to_gguf

T = TypeVar("T", bound=BaseModel)

class ResponseFormat(BaseModel):
    response: str


def get_response_structured(prompt, format:Type[T], llm) -> T:
    response =   llm(
            prompt,
            max_tokens=512,
            stop=["<|im_end|>"],  # Stop generation at the end token
            echo=False
        )

    output = response["choices"][0]["text"].strip()

    return format.model_validate_json(output)


class LLMResponseFormat(BaseModel):
    Concept_Explanation: str
    Code_Example: str
    PracticeExercise: str
    Feedback: str | None


def provide_structured_response(prompt):
    schema = LLMResponseFormat.model_json_schema()

    structured_prompt = f"""
    {prompt}

    You MUST respond with ONLY a valid JSON object. No explanation, no prose, no markdown.
    Your response must match this exact schema:
    {schema}
    """
    prompt = f"{structured_prompt}: {prompt}"
    return get_response_structured(prompt, LLMResponseFormat, llm)

