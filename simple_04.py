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

user_file = st.file_uploader(
    type=["txt", "md"],
    label="Upload Your File",
    accept_multiple_files=False,
    max_upload_size=2,  # Megabytes
)

if user_file:
    st.write(f"File Name: '{user_file.name}'")
    st.write(f"File Size: '{user_file.size}'")
    st.divider()
    # file_content_bytes: bytes = user_file.read()  # Binary
    file_content: str = user_file.read().decode(encoding="utf-8")
    st.markdown(file_content)

    # messages: list[dict] = []

    # system_prompt: str = "You are a useful AI assistant."
    # system_message: dict = {"role": "system", "content": system_prompt}
    # messages.append(system_message)

    # user_message: dict = {"role": "user", "content": user_prompt}
    # messages.append(user_message)

    # # NEW
    # assistant_answer, _, _ = chat(
    #     messages=messages,
    # )

    # if assistant_answer:
    #     with st.container(border=True):
    #         st.write(assistant_answer)
