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

# NEW
TITLE: Final[str] = "DT AI Dictionary!"

# NEW
SYSTEM_PROMPT: Final[str] = """
You are a professional translator assistant from English language to Farsi language.

User must write just one word in English language.

If user wrote more than one word 'Error! Try Again...'.

If user wrote one word but not in English language, answer 'Error! Try Again...'.

Just translate English word, based on the below instructions:

Write the translated to Farsi language of user word in ## part.
Write the English Pronounce of user word in ### part.
Write the 5 English Synonyms in #### parts.
Write the 2 English Antonyms in ##### parts.
Write the 2 sample and simple English sentences in ###### parts.

Just write the below text, based on above instructions and \
replace '##', ''###', '####', '#####', '######' \
with your answers and never write '#' in your result at all!

Translated to Farsi Language: ##
English Pronounce: ###

Synonyms:

1) ####
2) ####
3) ####
4) ####
5) ####

Antonyms:

1) #####
2) #####

Two Sample Sentences:

1) ######
2) ######
""".strip()

# NEW
TEMPERATURE: Final[float] = 0.0

# NEW
MODEL_NAME: Final[str] = "gemma4:e2b".replace(" ", "").lower()

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
