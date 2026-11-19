import streamlit as st

from typing import (
    Dict,
    List,
    Final,
)

from dt_lm import (
    ROLE_USER,
    ROLE_SYSTEM,
    KEY_NAME_ROLE,
    KEY_NAME_CONTENT,
    MESSAGE_NO_CONTENT_RECEIVED,
)

from dt_ollama import chat
from dt_utility import format_seconds

TITLE: Final[str] = "DT AI Chatbot!"

SYSTEM_PROMPT: Final[str] = """
You are a helpful AI assistant.
""".strip()

TEMPERATURE: Final[float] = 0.6
MODEL_NAME: Final[str] = "gemma3:1b".replace(" ", "").lower()

SYSTEM_MESSAGE: Final[Dict] = {
    KEY_NAME_ROLE: ROLE_SYSTEM,
    KEY_NAME_CONTENT: SYSTEM_PROMPT,
}

st.set_page_config(
    page_icon="👋",
    page_title=TITLE,
    layout="centered",
)

st.header(
    divider="rainbow",
    body=f"👋 {TITLE}",
)

user_prompt: str = st.text_input(
    icon="❓",
    label="User Prompt",
    label_visibility="hidden",
)

user_prompt = user_prompt.strip()

if user_prompt:
    messages: List[Dict] = []

    messages.append(SYSTEM_MESSAGE)

    user_message: Dict = {
        KEY_NAME_ROLE: ROLE_USER,
        KEY_NAME_CONTENT: user_prompt,
    }

    messages.append(user_message)

    assistant_answer, elapsed_time, prompt_tokens, completion_tokens = chat(
        messages=messages,
        model_name=MODEL_NAME,
        temperature=TEMPERATURE,
    )

    formatted_elapsed_time: str = format_seconds(seconds=elapsed_time)

    if not assistant_answer:
        assistant_answer = MESSAGE_NO_CONTENT_RECEIVED

    with st.container(border=True):
        st.write(assistant_answer)

    prompt_tokens_message: str = f"Input Tokens: {prompt_tokens}"
    completion_tokens_message: str = f"Output Tokens: {completion_tokens}"
    formatted_elapsed_time_message: str = f"Elapsed Time: {formatted_elapsed_time}"
    message: str = f"{prompt_tokens_message} - {completion_tokens_message} - {formatted_elapsed_time_message}"
    st.caption(message)
