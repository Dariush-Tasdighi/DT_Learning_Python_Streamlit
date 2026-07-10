import streamlit as st
from typing import Final

PAGE_TITLE: Final[str] = "DT Chatbot!"
USER_QUESTION: Final[str] = "Enter your prompt"


def chat(user_prompt: str) -> str:
    """
    Chat
    """

    assistant_answer: str = f"I don't know! {user_prompt}"
    return assistant_answer


# NEW
def initialize(page_title: str) -> None:
    """
    Initialize
    """

    st.set_page_config(
        page_icon="👋",
        layout="centered",
        page_title=page_title,
    )


# NEW
def show_main_section() -> None:
    """
    Show main section
    """

    st.header(
        divider="rainbow",
        body=f"👋 {PAGE_TITLE}",
    )

    user_prompt = st.text_input(
        icon="❓",
        label=USER_QUESTION,
    )

    user_prompt = user_prompt.strip()

    if user_prompt:
        assistant_answer = chat(user_prompt=user_prompt)

        if assistant_answer:
            with st.container(border=True):
                st.write(assistant_answer)


# NEW
initialize(page_title=PAGE_TITLE)
show_main_section()
