import streamlit as st

from ollama import chat
from typing import (
    Final,
    Optional,
)

TITLE: Final[str] = "DT AI Chatbot!"

st.set_page_config(
    page_icon="👋",
    page_title=TITLE,
    layout="centered",
)

st.header(
    divider="rainbow",
    body=f"👋 {TITLE}",
)

user_prompt = st.text_input(
    # NEW
    icon="❓",
    #
    label="Enter your prompt",
)

user_prompt = user_prompt.strip()

if user_prompt:
    messages: list[dict] = []

    user_message: dict = {"role": "user", "content": user_prompt}
    messages.append(user_message)

    response = chat(
        model="gemma3:1b",
        messages=messages,
    )

    assistant_answer: Optional[str] = response.message.content

    if assistant_answer:
        # st.write(assistant_answer)

        # NEW
        with st.container(border=True):
            st.write(assistant_answer)
