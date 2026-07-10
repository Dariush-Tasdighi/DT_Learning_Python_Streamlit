"""
Dariush Tasdighi Streamlit Authenticator Module
"""

import streamlit as st
import dt_utility as utility

from typing import Final
from streamlit.delta_generator import DeltaGenerator

VERSION: Final[str] = "1.1.0"

_HEADER_LOGIN: Final[str] = "Login"

_LABEL_LOGIN: Final[str] = "Login"
_LABEL_LOGOUT: Final[str] = "Logout"
_LABEL_USERNAME: Final[str] = "Username"
_LABEL_PASSWORD: Final[str] = "Password"

SESSION_STATE_KEY_USERNAME: Final[str] = "username"
SESSION_STATE_KEY_USER_LOGGED_IN: Final[str] = "user_logged_in"

_ERROR_MESSAGE_WRONG_USERNAME_PASSWORD: Final[str] = (
    "Username and/or password is not correct!"
)


def _login(username: str, password: str) -> bool:
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

    if SESSION_STATE_KEY_USERNAME not in st.session_state:
        st.session_state[SESSION_STATE_KEY_USERNAME] = ""

    if SESSION_STATE_KEY_USER_LOGGED_IN not in st.session_state:
        st.session_state[SESSION_STATE_KEY_USER_LOGGED_IN] = False


def _login_button_clicked_callback(username: str, password: str) -> None:
    """
    Login button clicked callback
    """

    result: bool = _login(username=username, password=password)

    if result:
        st.session_state[SESSION_STATE_KEY_USERNAME] = username
        st.session_state[SESSION_STATE_KEY_USER_LOGGED_IN] = True
    else:
        st.error(body=_ERROR_MESSAGE_WRONG_USERNAME_PASSWORD)


def _logout_button_clicked_callback() -> None:
    """
    Logout button clicked callback
    """

    st.session_state[SESSION_STATE_KEY_USERNAME] = ""
    st.session_state[SESSION_STATE_KEY_USER_LOGGED_IN] = False


def show_login_section() -> None:
    """
    Show login section
    """

    login_section = st.container(border=True)

    with login_section:
        st.header(
            divider="rainbow",
            body=f"👋 {_HEADER_LOGIN}",
        )

        username: str = st.text_input(label=_LABEL_USERNAME)
        password: str = st.text_input(label=_LABEL_PASSWORD)
        # password: str = st.text_input(label=_LABEL_PASSWORD, type="password")

        username = username.strip()
        password = password.strip()

        st.button(
            label=_LABEL_LOGIN,
            args=(username, password),
            on_click=_login_button_clicked_callback,
        )


def show_logout_section(container: DeltaGenerator) -> None:
    """
    Show logout section
    """

    with container:
        username: str = st.session_state[SESSION_STATE_KEY_USERNAME]
        st.write(f"Welcome {username}!")

        st.button(
            label=_LABEL_LOGOUT,
            on_click=_logout_button_clicked_callback,
        )

        st.divider()


if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
