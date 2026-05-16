from model import tokenizer, llm
from system_prompt import system_prompt
def get_qwen_chat_prompt(messages):
    # Create a conversation system prompt if needed

    conversation = []

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
