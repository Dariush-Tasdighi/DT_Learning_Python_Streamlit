import streamlit as st

# NEW
from typing import Final

# NEW
PAGE_TITLE: Final[str] = "DT Chatbot!"
USER_QUESTION: Final[str] = "Enter your prompt"


def chat(user_prompt: str) -> str:
    """
    Chat
    """

    assistant_answer: str = f"I don't know! {user_prompt}"
    return assistant_answer


st.set_page_config(
    page_icon="👋",
    layout="centered",
    # NEW
    page_title=PAGE_TITLE,
)

st.header(
    divider="rainbow",
    # NEW
    body=f"👋 {PAGE_TITLE}",
)

user_prompt: str = st.text_input(
    icon="❓",
    # NEW
    label=USER_QUESTION,
)

user_prompt = user_prompt.strip()

if user_prompt:
    assistant_answer: str = chat(user_prompt=user_prompt)

    if assistant_answer:
        with st.container(border=True):
            st.write(assistant_answer)
