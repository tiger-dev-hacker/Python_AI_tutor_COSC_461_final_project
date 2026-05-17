from idna import decode
from structured_response import provide_structured_response, decode_response

def chatbot(prompt):
    # Start the loop
    print("Qwen Chatbot started. Type 'quit' to exit")

    chat_history = []

    if prompt.lower() == 'quit':
        return "quit"

    chat_history.append({"role": "user", "content": prompt})

    output = provide_structured_response(prompt)

    chat_history.append({"role": "assistant", "content": output})

    return decode_response(output)

