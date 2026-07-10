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
        # NEW
        st.subheader(body=constants.HEADER_SETTINGS, divider="rainbow")

        # NEW
        st.button(
            label=authenticator.LABEL_LOGOUT,
            on_click=authenticator.logout_button_clicked,
        )


def show_main_section() -> None:
    """
    Show main section
    """

    st.header(
        divider="rainbow",
        # NEW
        body=f"👋 {constants.PAGE_TITLE}",
    )

    user_prompt = st.text_input(
        icon="❓",
        # NEW
        label=constants.USER_QUESTION,
    )

    user_prompt = user_prompt.strip()

    if user_prompt:
        assistant_answer = chat(user_prompt=user_prompt)

        if assistant_answer:
            with st.container(border=True):
                st.write(assistant_answer)


# NEW
authenticator.initialize(page_title=constants.PAGE_TITLE)
if st.session_state.user_logged_in:
    show_main_section()
    show_sidebar_section()
else:
    authenticator.show_login_section()
