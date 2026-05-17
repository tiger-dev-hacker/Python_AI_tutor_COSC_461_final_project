from system_prompt import system_prompt
from model import llm
from pydantic import BaseModel
from typing import Optional
import json

alphabets  = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# The JSON schema that the model must follow
class LLMResponseFormat(BaseModel):
    Concept_Explanation: str
    Code_Example: str
    Practice_Exercise: list[str]
    Feedback_and_Debugging: Optional[str] = None


def provide_structured_response(user_input):
    try:
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
        raw =  output['choices'][0]['message']['content']
        answer =  LLMResponseFormat(**json.loads(raw))
    except Exception as e:

        answer =  LLMResponseFormat(
            Concept_Explanation=str(e),
            Code_Example="Cannot provided examples at this time",
            Practice_Exercise=["No practice exercise provided"],
            Feedback_and_Debugging="Not available at the end",
        )

    return decode_response(answer)

def decode_response(object):
    response_dict = object.model_dump()

    response_key = ""

    count = 1
    for key in response_dict:
        if response_dict[key] is not None:
            if isinstance(response_dict[key], list):
                response_key += f"\n {count}. {key}: \n"
                for i, problem in enumerate(response_dict[key]):
                    response_key += f" {alphabets[i % 26]}. {problem}\n"
            else:
                response_key += f"\n {count}.  {key}: {response_dict[key]}\n"
        count += 1

    return response_key