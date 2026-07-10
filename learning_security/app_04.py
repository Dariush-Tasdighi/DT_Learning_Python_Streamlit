import streamlit as st
from typing import Final

PAGE_TITLE: Final[str] = "DT Chatbot!"
USER_QUESTION: Final[str] = "Enter your prompt"

# NEW
LABEL_LOGIN: Final[str] = "Login"
HEADER_LOGIN: Final[str] = "Login"
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


# NEW
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

    # NEW
    if "user_logged_in" not in st.session_state:
        st.session_state.user_logged_in = False


# NEW
def login_button_clicked_callback(username: str, password: str) -> None:
    """
    Login button clicked callback
    """

    result: bool = login(username=username, password=password)

    if result:
        st.session_state.user_logged_in = True
    else:
        st.error(body=ERROR_MESSAGE_WRONG_USERNAME_PASSWORD)


# NEW
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

        username: str = st.text_input(label=LABEL_USERNAME)
        password: str = st.text_input(label=LABEL_PASSWORD)
        # password: str = st.text_input(label=LABEL_PASSWORD, type="password")

        username = username.strip()
        password = password.strip()

        # ********************
        # دستورات ذیل، درست کار نمی‌کنند
        # ********************
        # login_button_clicked: bool = st.button(label=LABEL_LOGIN)

        # if login_button_clicked:
        #     result: bool = login(
        #         username=username,
        #         password=password,
        #     )

        #     if result:
        #         st.session_state.user_logged_in = True
        #     else:
        #         st.error(body=ERROR_MESSAGE_WRONG_USERNAME_PASSWORD)
        # ********************

        st.button(
            label=LABEL_LOGIN,
            args=(username, password),
            on_click=login_button_clicked_callback,
        )


def show_main_section() -> None:
    """
    Show main section
    """

    st.header(
        divider="rainbow",
        body=f"👋 {PAGE_TITLE}",
    )

    user_prompt: str = st.text_input(
        icon="❓",
        label=USER_QUESTION,
    )

    user_prompt = user_prompt.strip()

    if user_prompt:
        assistant_answer: str = chat(user_prompt=user_prompt)

        if assistant_answer:
            with st.container(border=True):
                st.write(assistant_answer)


initialize(page_title=PAGE_TITLE)
# NEW
if st.session_state.user_logged_in:
    show_main_section()
else:
    show_login_section()
