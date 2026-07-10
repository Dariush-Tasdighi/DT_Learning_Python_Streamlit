"""
Dariush Tasdighi Streamlit Authenticator Module
"""

from typing import Final

import streamlit as st
import dt_utility as utility

VERSION: Final[str] = "1.0.0"

HEADER_LOGIN: Final[str] = "Login"

LABEL_LOGIN: Final[str] = "Login"
LABEL_LOGOUT: Final[str] = "Logout"
LABEL_USERNAME: Final[str] = "Username"
LABEL_PASSWORD: Final[str] = "Password"

ERROR_MESSAGE_WRONG_USERNAME_PASSWORD: Final[str] = (
    "Username and/or password is not correct!"
)


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


if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
