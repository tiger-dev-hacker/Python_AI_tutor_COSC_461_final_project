from system_prompt import system_prompt
from model import llm
from pydantic import BaseModel


class LLMResponseFormat(BaseModel):
    Concept_Explanation: str
    Code_Example: str
    PracticeExercise: str
    Feedback: str | None


def provide_structured_response(user_input):
    output = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],

        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "python tutor format",
                "schema": LLMResponseFormat.model_json_schema()
            }
        },
        temperature=0.1
    )

    # Extract and print response
    return output['choices'][0]['message']['content']