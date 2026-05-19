---
license: mit
---
# PyGuru – AI Python Tutor

A locally-hosted, conversational Python tutoring application powered by a quantized large language model. PyGuru runs entirely on your own hardware — no API keys, no cloud calls, no data leaving your machine.

---

## Features

- **Structured responses** — every reply is enforced to include a concept explanation, code example, practice exercise, and optional debugging feedback
- **Streaming output** — responses render token-by-token for a responsive chat experience
- **Fully local inference** — runs on-device via `llama-cpp-python` with GPU acceleration support
- **Session management** — persistent chat history within a session; type `quit` to reset
- **Graceful error handling** — model failures surface as readable messages rather than crashes

---

## Tech Stack

| Layer | Tool |
|---|---|
| UI | [Streamlit](https://streamlit.io/) |
| Inference | [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) |
| Model | Qwen2.5-Coder-7B-Instruct (Q5_K_M GGUF) |
| Schema | [Pydantic v2](https://docs.pydantic.dev/) |
| Tokenizer | [HuggingFace Transformers](https://huggingface.co/docs/transformers) |

---

## Requirements

- Python 3.9+
- A GPU with ~6 GB VRAM (or Apple Silicon with sufficient unified memory)
- The model file: `qwen2.5-coder-7b-instruct-q5_k_m.gguf` placed in the project root

Install dependencies:

```bash
pip install streamlit llama-cpp-python pydantic transformers json typing
```

> For GPU acceleration, install `llama-cpp-python` with the appropriate backend flag.  
> See the [llama-cpp-python docs](https://github.com/abetlen/llama-cpp-python#installation-with-hardware-acceleration) for CUDA, Metal, and other options.

---

## Project Structure

```
pyguru/
├── app.py                   # Streamlit chat interface
├── chat.py                     # Implementation of chatbot with command line, used in app
├── structured_response.py   # Response schema, model invocation, error handling
├── model.py                 # LLM and tokenizer initialization
├── system_prompt.py         # System prompt definition
└── README.md               # Description of the project and setup for future contribution or validation


```

---

## Usage

```bash
streamlit run app.py
```

Open the URL printed in your terminal (typically `http://localhost:8501`), then ask any Python question in the chat box. Type `quit` to clear the session and start over.

---

## Response Format

Every answer follows this schema:

```
1. Concept_Explanation   — plain-language explanation of the topic
2. Code_Example          — a working Python snippet
3. Practice_Exercise     — one or more exercises to attempt
4. Feedback_and_Debugging (optional) — targeted feedback on errors or edge cases
5. Refactor (optional and advanced) - suggests ways to refactor code or improve design
```

---

## Model

PyGuru uses **Qwen2.5-Coder-7B-Instruct**, a code-specialized language model from Alibaba, in its Q5_K_M GGUF quantized form. You can download it from [HuggingFace](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF).

---

## License

MIT