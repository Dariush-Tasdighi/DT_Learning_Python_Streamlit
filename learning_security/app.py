import streamlit as st
import app_constants as constants
import dt_streamlit_authenticator as authenticator


def chat(user_prompt: str) -> str:
    """
    Chat
    """

    assistant_answer: str = f"I don't know! {user_prompt}"
    return assistant_answer


def show_sidebar_section() -> None:
    """
    Show sidebar section
    """

    sidebar_section = st.sidebar

    with sidebar_section:
        st.subheader(body=constants.HEADER_SETTINGS, divider="rainbow")

        authenticator.show_logout_section(container=sidebar_section)


def show_main_section() -> None:
    """
    Show main section
    """

    st.header(
        divider="rainbow",
        body=f"👋 {constants.PAGE_TITLE}",
    )

    user_prompt: str = st.text_input(
        icon="❓",
        label=constants.USER_QUESTION,
    )

    user_prompt = user_prompt.strip()

    if user_prompt:
        assistant_answer: str = chat(user_prompt=user_prompt)

        if assistant_answer:
            with st.container(border=True):
                st.write(assistant_answer)


authenticator.initialize(page_title=constants.PAGE_TITLE)

if st.session_state.user_logged_in:
    show_main_section()
    show_sidebar_section()
else:
    authenticator.show_login_section()
