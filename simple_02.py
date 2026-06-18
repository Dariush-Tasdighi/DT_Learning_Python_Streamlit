import streamlit as st

from typing import Final
from dtx_ollama import chat

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
    icon="❓",
    label="Enter your prompt",
)

user_prompt = user_prompt.strip()

if user_prompt:
    messages: list[dict] = []

    system_prompt: str = "You are a useful AI assistant."
    system_message: dict = {"role": "system", "content": system_prompt}
    messages.append(system_message)

    user_message: dict = {"role": "user", "content": user_prompt}
    messages.append(user_message)

    # NEW
    assistant_answer, _, _ = chat(
        messages=messages,
    )

    if assistant_answer:
        with st.container(border=True):
            st.write(assistant_answer)
