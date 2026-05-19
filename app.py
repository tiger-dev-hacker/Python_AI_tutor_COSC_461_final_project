import streamlit as st
import random
import time
from structured_response import provide_structured_response
from structured_response import alphabets

st.title("PyGuru - AI python tutor")

# Initialize chat history

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = ""
# Accept user input
if prompt := st.chat_input("Welcome to Python Tutoring! I am an AI-based python tutor. How can I help you today?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

        # --- Reset session on "quit" ---
    if prompt.strip().lower() == "quit":
        st.session_state.messages = []
        st.rerun()

    st.session_state.messages.append({"role": "user", "content": prompt})

# Streamed response emulator
def response_generator(prompt):
    response_dict = provide_structured_response(prompt).model_dump()

    count = 1
    for key in response_dict:
        if response_dict[key] is not None:
            if isinstance(response_dict[key], list):
                yield f"\n\n {count}. {key}: \n\n"

                for i, problem in enumerate(response_dict[key]):
                    yield f" {alphabets[i % 26] }:  "
                    for c in problem.split(" "):
                        yield c + " "
                    yield "\n\n"

            else:
                yield f"\n\n {count}.  {key}: "

                for c in response_dict[key].split(" "):
                    yield c + " "

        count += 1

# Display assistant response in chat message container
with st.chat_message("assistant"):
    if not prompt:
        st.write("How can I help you today?")
    else:
        response = st.write_stream(response_generator(prompt))
        st.session_state.messages.append({"role": "assistant", "content": response})
