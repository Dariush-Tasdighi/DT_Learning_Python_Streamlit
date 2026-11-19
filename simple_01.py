import streamlit as st

from typing import (
    Dict,
    List,
    Final,
    Optional,
)

from ollama import (
    chat,
    ChatResponse,
)

TITLE: Final[str] = "DT AI Chatbot!"

SYSTEM_PROMPT: Final[str] = """
You are a helpful AI assistant.
""".strip()

st.set_page_config(
    page_icon="👋",
    page_title=TITLE,
    layout="centered",
)

st.header(
    divider="rainbow",
    body=f"👋 {TITLE}",
)

# user_prompt: str = input("User: ")

user_prompt: str = st.text_input(
    # NEW
    icon="❓",
    #
    label="Enter your prompt",
)

user_prompt = user_prompt.strip()

if user_prompt:
    messages: List[Dict] = []

    system_message: Dict = {"role": "system", "content": SYSTEM_PROMPT}
    messages.append(system_message)

    user_message: Dict = {"role": "user", "content": user_prompt}
    messages.append(user_message)

    response: ChatResponse = chat(
        model="gemma3:1b",
        messages=messages,
    )

    assistant_answer: Optional[str] = response.message.content

    if assistant_answer:
        # st.write(assistant_answer)

        # NEW
        with st.container(border=True):
            st.write(assistant_answer)
