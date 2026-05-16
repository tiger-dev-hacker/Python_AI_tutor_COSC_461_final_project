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
