from system_prompt import system_prompt
from model import llm
from pydantic import BaseModel
from typing import Optional
import json


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
        return LLMResponseFormat(**json.loads(raw))
    except Exception as e:

        return LLMResponseFormat(
            Concept_Explanation=str(e),
            Code_Example="Cannot provided examples at this time",
            Practice_Exercise=["No practice exercise provided"],
            Feedback_and_Debugging="Not available at the end",
        )

def decode_response(object):
    response_dict = object.model_dump()

    response_key = ""
    for key in response_dict:
        if response_dict[key] is not None:
            if isinstance(response_dict[key], list):
                response_key += f"\n{key}: \n"
                for problem in response_dict[key]:
                    response_key += f"- {problem}\n"
            else:
                response_key += f"\n - {key}: {response_dict[key]}\n"


    return response_key