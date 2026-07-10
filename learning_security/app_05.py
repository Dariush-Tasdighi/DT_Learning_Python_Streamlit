import streamlit as st
from typing import Final

# NEW
from streamlit.delta_generator import DeltaGenerator

PAGE_TITLE: Final[str] = "DT Chatbot!"
USER_QUESTION: Final[str] = "Enter your prompt"

HEADER_LOGIN: Final[str] = "Login"
# NEW
HEADER_SETTINGS: Final[str] = "Settings"

LABEL_LOGIN: Final[str] = "Login"
# NEW
LABEL_LOGOUT: Final[str] = "Logout"

LABEL_USERNAME: Final[str] = "Username"
LABEL_PASSWORD: Final[str] = "Password"

# NEW
SESSION_STATE_KEY_USERNAME: Final[str] = "username"
SESSION_STATE_KEY_USER_LOGGED_IN: Final[str] = "user_logged_in"

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

    # NEW
    # if "user_logged_in" not in st.session_state:
    #     st.session_state.user_logged_in = False

    # NEW
    if SESSION_STATE_KEY_USERNAME not in st.session_state:
        st.session_state[SESSION_STATE_KEY_USERNAME] = ""

    # NEW
    if SESSION_STATE_KEY_USER_LOGGED_IN not in st.session_state:
        st.session_state[SESSION_STATE_KEY_USER_LOGGED_IN] = False


def login_button_clicked_callback(username: str, password: str) -> None:
    """
    Login button clicked callback
    """

    result: bool = login(username=username, password=password)

    if result:
        # NEW
        # st.session_state.user_logged_in = True
        st.session_state[SESSION_STATE_KEY_USERNAME] = username
        st.session_state[SESSION_STATE_KEY_USER_LOGGED_IN] = True
    else:
        st.error(body=ERROR_MESSAGE_WRONG_USERNAME_PASSWORD)


# NEW
def logout_button_clicked_callback() -> None:
    """
    Logout button clicked callback
    """

    # NEW
    # st.session_state.user_logged_in = False
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
            body=f"👋 {HEADER_LOGIN}",
        )

        username: str = st.text_input(label=LABEL_USERNAME)
        password: str = st.text_input(label=LABEL_PASSWORD)
        # password: str = st.text_input(label=LABEL_PASSWORD, type="password")

        username = username.strip()
        password = password.strip()

        st.button(
            label=LABEL_LOGIN,
            args=(username, password),
            on_click=login_button_clicked_callback,
        )


# NEW
def show_logout_section(container: DeltaGenerator) -> None:
    """
    Show logout section
    """

    with container:
        st.button(
            label=LABEL_LOGOUT,
            on_click=logout_button_clicked_callback,
        )


# NEW
def show_sidebar_section() -> None:
    """
    Show sidebar section
    """

    sidebar_section = st.sidebar

    with sidebar_section:
        st.subheader(body=HEADER_SETTINGS, divider="rainbow")

        show_logout_section(container=sidebar_section)


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
if st.session_state.user_logged_in:
    show_main_section()
    # NEW
    show_sidebar_section()
else:
    show_login_section()
