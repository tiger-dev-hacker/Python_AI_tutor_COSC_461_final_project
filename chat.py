from llama_cpp import Llama
from transformers import AutoTokenizer

path = "qwen2.5-coder-7b-instruct-q5_k_m.gguf"
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")

llm = Llama(
    model_path=path,
    n_gpu_layers=-1,
    n_ctx=4096,
    verbose=False
)


def get_qwen_chat_prompt(messages):
    # Create a conversation system prompt if needed

    conversation = []

    system_prompt = r"""
        You are an experienced python tutor with a huge experience of teaching python to students. For every request provided by user to learn python, structure the response into three parts, 
        Concept Explanation, Code Example, Practice Exercise, and optionally feedback and debugging help if a user inputs a python code samples. Adhere to this structure as strictly as possible. 
        1. Explain the underlying concept that the user asks or inside the code snippet, if a code snippet is included.
        2. Include similar code examples explaining the same concept under the Code Example section.
        3. Include at least one or more practice exercise problems inside the Practice Exercise section to allow the user to solidify its concepts.
        4. This is optional but if  the user asks for feedback on a code sample or asks for debugging help, include feedback or debugging tips in the Feedback/tips section.
        
        Based on the user input, shift the focus on each section accordingly. For instance, if the user asks for explanation or includes words like
        "explain", focus more on explanation. If the user asks for practice examples or includes words like "exercise", focus more on providing practice exercise problems (at least 3-5 problems),
        . If the user input include code snippets or includes keywords like "debug" or "feedback", then focus more on providing proper feedback, suggestions and debugging tips.
        
        Do not hallucinate and do not include incorrect information and strictly adhere to the four-part structure as described above.
    """
    if messages:
        conversation.extend(messages)
    else:
        conversation.append({"role": "system", "content": system_prompt})

    # Apply the chat template
    prompt = tokenizer.apply_chat_template(
        conversation,
        tokenize=False,
        add_generation_prompt=True
    )

    return prompt


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