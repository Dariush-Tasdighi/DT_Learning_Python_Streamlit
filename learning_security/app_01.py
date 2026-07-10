import streamlit as st


def chat(user_prompt: str) -> str:
    """
    Chat
    """

    assistant_answer: str = f"I don't know! {user_prompt}"
    return assistant_answer


st.set_page_config(
    page_icon="👋",
    page_title="DT Chatbot!",
    layout="centered",
)

st.header(
    divider="rainbow",
    body=f"👋 DT Chatbot!",
)

user_prompt: str = st.text_input(
    icon="❓",
    label="Enter your prompt",
)

user_prompt = user_prompt.strip()

if user_prompt:
    assistant_answer: str = chat(user_prompt=user_prompt)

    if assistant_answer:
        with st.container(border=True):
            st.write(assistant_answer)
