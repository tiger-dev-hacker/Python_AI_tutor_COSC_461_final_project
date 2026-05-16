from model import llm
from utils import get_qwen_chat_prompt
from structured_response import provide_structured_response, LLMResponseFormat
from system_prompt import system_prompt

def chatbot():
    # Start the loop
    print("Qwen Chatbot started. Type 'quit' to exit")

    chat_history = []

    while True:
        user_input = input("Enter a response: ")

        if user_input.lower() == 'quit':
            break

        chat_history.append({"role": "user", "content": user_input})

        # prompt = get_qwen_chat_prompt(chat_history)

        output = llm.create_chat_completion(
            messages = [
                { "role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],

            response_format = {
                "type": "json_schema",
                "json_schema": {
                    "name": "python tutor format",
                    "schema": LLMResponseFormat.model_json_schema()
                }
            },
            temperature=0.1
        )

        # Extract and print response
        response = output['choices'][0]['message']['content']  # ✅ the actual text


        print(f"Assistant response: {response}")
        #
        #
        # chat_history.append({"role": "assistant", "content": assistant_response})



if __name__ == "__main__":
    chatbot()