from model import llm
from utils import get_qwen_chat_prompt


def chatbot():
    # Start the loop
    print("Qwen Chatbot started. Type 'quit' to exit")

    chat_history = []

    while True:
        user_input = input("Enter a response: ")

        if user_input.lower() == 'quit':
            break

        chat_history.append({"role": "user", "content": user_input})

        prompt = get_qwen_chat_prompt(chat_history)

        output = llm(
            prompt,
            max_tokens=512,
            stop=["<|im_end|>"],  # Stop generation at the end token
            echo=False
        )

        # Extract and print response
        assistant_response = output["choices"][0]["text"].strip()

        print(f"Assistant: {assistant_response}")

        chat_history.append({"role": "assistant", "content": assistant_response})



if __name__ == "__main__":
    chatbot()