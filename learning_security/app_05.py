import streamlit as st
from typing import Final

PAGE_TITLE: Final[str] = "DT Chatbot!"
USER_QUESTION: Final[str] = "Enter your prompt"

HEADER_LOGIN: Final[str] = "Login"
# NEW
HEADER_SETTINGS: Final[str] = "Settings"

LABEL_LOGIN: Final[str] = "Login"
# NEW
LABEL_LOGOUT: Final[str] = "Logout"
#
LABEL_USERNAME: Final[str] = "Username"
LABEL_PASSWORD: Final[str] = "Password"

ERROR_MESSAGE_WRONG_USERNAME_PASSWORD: Final[str] = (
    "Username and/or password is not correct!"
)


def chat(user_prompt: str) -> str:
    """
    Chat
    """

    assistant_answer: str = f"I don't know! {user_prompt}"
    return assistant_answer


def login(username: str, password: str) -> bool:
    """
    Login
    """

    if username == "admin" and password == "admin":
        return True
    else:
        return False


def initialize(page_title: str) -> None:
    """
    Initialize
    """

    st.set_page_config(
        page_icon="👋",
        layout="centered",
        page_title=page_title,
    )

    if "user_logged_in" not in st.session_state:
        st.session_state.user_logged_in = False


def login_button_clicked(username: str, password: str) -> None:
    """
    Login button clicked
    """

    login_result: bool = login(username=username, password=password)
    if login_result:
        st.session_state.user_logged_in = True
    else:
        st.error(body=ERROR_MESSAGE_WRONG_USERNAME_PASSWORD)


# NEW
def logout_button_clicked() -> None:
    """
    Logout
    """

    st.session_state.user_logged_in = False


def show_login_section() -> None:
    """
    Show login section
    """

    login_section = st.container(border=True)
    with login_section:
        st.header(
            divider="rainbow",
            body=f"👋 {HEADER_LOGIN}",
        )

        username_text_input = st.text_input(label=LABEL_USERNAME)
        password_text_input = st.text_input(label=LABEL_PASSWORD)
        # password_text_input = st.text_input(label=LABEL_PASSWORD, type="password")

        username: str = username_text_input.strip()
        password: str = password_text_input.strip()

        st.button(
            label=LABEL_LOGIN,
            args=(username, password),
            on_click=login_button_clicked,
        )


# NEW
def show_sidebar_section() -> None:
    """
    Show sidebar section
    """

    sidebar_section = st.sidebar
    with sidebar_section:
        st.subheader(body=HEADER_SETTINGS, divider="rainbow")

        st.button(
            label=LABEL_LOGOUT,
            on_click=logout_button_clicked,
        )


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


initialize(page_title=PAGE_TITLE)
if st.session_state.user_logged_in:
    show_main_section()
    # NEW
    show_sidebar_section()
else:
    show_login_section()
