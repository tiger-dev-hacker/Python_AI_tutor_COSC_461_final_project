import streamlit as st
import random
import time
from structured_response import provide_structured_response

st.title("Simple chat")

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


    st.session_state.messages.append({"role": "user", "content": prompt})

# Streamed response emulator
def response_generator(prompt):
    response = provide_structured_response(prompt)

    print(response)
    for word in response.split(" "):
        prev_char = word
        if word == "." and prev_char == word.isdigit():
            yield f"{word}"

        yield word + " "
        time.sleep(0.05)

# Display assistant response in chat message container
with st.chat_message("assistant"):
    if prompt is None:
        st.write("How can I help you today?")
    else:
        response = st.write_stream(response_generator(prompt))
        st.session_state.messages.append({"role": "assistant", "content": response})
