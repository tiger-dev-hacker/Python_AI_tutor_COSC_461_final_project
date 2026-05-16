from structured_response import provide_structured_response

def chatbot():
    # Start the loop
    print("Qwen Chatbot started. Type 'quit' to exit")

    chat_history = []

    while True:
        user_input = input("Enter a response: ")

        if user_input.lower() == 'quit':
            break

        chat_history.append({"role": "user", "content": user_input})

        output = provide_structured_response(user_input)

        print(f"Assistant response:\n {output}")

        chat_history.append({"role": "assistant", "content": output})



if __name__ == "__main__":
    chatbot()