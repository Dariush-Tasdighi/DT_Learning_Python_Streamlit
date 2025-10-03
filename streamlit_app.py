# **************************************************
# For Running:
# > python .\streamlit_app.py
# **************************************************
# import streamlit

# print(f"Version of 'streamlit' package: {streamlit.__version__}")
# **************************************************


# **************************************************
# For Running:
# > python .\streamlit_app.py
# **************************************************
# Bad Practice:
# import os, streamlit
# **************************************************
# import os
# import streamlit

# os.system(command="cls" if os.name == "nt" else "clear")

# print(f"Version of 'streamlit' package: {streamlit.__version__}")
# print()
# **************************************************


# **************************************************
# For Running:
# > python .\streamlit_app.py
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls" if os.name == "nt" else "clear")

# print(f"Version of 'streamlit' package: {st.__version__}")
# print()
# **************************************************


# **************************************************
# Notes:
#
# 1) app.py / main.py          --> streamlit_app.py
# 2) python ./streamlit_app.py --> streamlit run ./streamlit_app.py
# **************************************************


# **************************************************
# For Running:
# > streamlit run ./streamlit_app.py
# **************************************************
# - https://www.w3schools.com
#   - https://www.w3schools.com/css/default.asp
#   - https://www.w3schools.com/html/default.asp
# **************************************************
# import os
# import streamlit as st

# # است Bad Practice ،Streamlit در پروژه‌های
# os.system(command="cls" if os.name == "nt" else "clear")

# st.write("Hello, World!")  # <p>
# **************************************************


# **************************************************
# Note: Do Not Write Below Codes!
#
# import os
# os.system(command="cls" if os.name == "nt" else "clear")
# **************************************************


# **************************************************
# import streamlit as st

# st.write("Hello, World!")  # <p>
# **************************************************


# **************************************************
# import streamlit as st

# st.write("Hello, World!")
# st.write("I'm Dariush Tasdighi!")
# **************************************************


# **************************************************
# In One Line!
# **************************************************
# import streamlit as st

# st.write("Hello, World!", "I'm Dariush Tasdighi!")
# **************************************************


# **************************************************
# Using Markdown
# **************************************************
# import streamlit as st

# st.header(body="Dariush Tasdighi (1)")  # <h2> --> Best Practice

# st.markdown(body="## Dariush Tasdighi (2)")  # <h2>

# st.markdown(body="<h2>Dariush Tasdighi (3)</h2>")  # می‌کند Encode به خاطر مسائل امنیتی

# st.markdown(body="<h2>Dariush Tasdighi (4)</h2>", unsafe_allow_html=True)
# **************************************************


# **************************************************
# import streamlit as st

# st.header(body="Sample (1)")

# st.markdown(body="# Dariush Tasdighi (1)")
# st.markdown(body="## Dariush Tasdighi (2)")
# st.markdown(body="### Dariush Tasdighi (3)")
# st.markdown(body="#### Dariush Tasdighi (4)")
# st.markdown(body="##### Dariush Tasdighi (5)")
# st.markdown(body="###### Dariush Tasdighi (6)")
# st.divider()  # <hr>

# st.header(body="Sample (2)")

# st.write("# Dariush Tasdighi (1)")
# st.write("## Dariush Tasdighi (2)")
# st.write("### Dariush Tasdighi (3)")
# st.write("#### Dariush Tasdighi (4)")
# st.write("##### Dariush Tasdighi (5)")
# st.write("###### Dariush Tasdighi (6)")
# st.divider()

# # body = """# Dariush Tasdighi
# # ## Dariush Tasdighi
# # ### Dariush Tasdighi
# # #### Dariush Tasdighi
# # ##### Dariush Tasdighi
# # ###### Dariush Tasdighi"""

# # body = """\
# # # Dariush Tasdighi
# # ## Dariush Tasdighi
# # ### Dariush Tasdighi
# # #### Dariush Tasdighi
# # ##### Dariush Tasdighi
# # ###### Dariush Tasdighi\
# # """

# st.header(body="Sample (3)")

# body = """
# # Dariush Tasdighi
# ## Dariush Tasdighi
# ### Dariush Tasdighi
# #### Dariush Tasdighi
# ##### Dariush Tasdighi
# ###### Dariush Tasdighi
# """

# st.markdown(body=body)
# st.divider()
# **************************************************


# **************************************************
# Emoji:
#
# https://gitlab.com/-/snippets/2526872
# https://gist.github.com/rxaviers/7360908
# https://gohugo.io/quick-reference/emojis
# https://github.com/ikatyang/emoji-cheat-sheet
# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app
# https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia
#
# Material:
#
# https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
# **************************************************


# **************************************************
# import streamlit as st

# st.set_page_config(page_title="Dariush Tasdighi", page_icon="👋")
# # st.set_page_config(page_title="Dariush Tasdighi", page_icon=":wave:")
# # st.set_page_config(
# #     layout="wide",  # Default: "centered"
# #     page_icon="👋",
# #     page_title="Dariush Tasdighi",
# # )

# st.header(body="I'm Dariush Tasdighi")
# **************************************************


# **************************************************
# import streamlit as st

# st.set_page_config(
#     page_icon="👋",
#     page_title="Dariush Tasdighi",
# )

# st.header(body="Dariush")
# st.divider()
# st.header(body="👋 Dariush")
# st.divider()
# st.header(body=":wave: Dariush")
# st.divider()

# # “blue”, “green”, “orange”, “red”, “violet”, “gray”/"grey", or “rainbow”
# st.header(body="Dariush", divider="rainbow")
# **************************************************


# **************************************************
# title()   -> Does not have divider
# header()  -> Has divider
# subheader -> Has divider
# **************************************************
# import streamlit as st

# st.title(body="👋 Welcome to My Site!")  # <h1>
# st.header(body="👋 Welcome to My Site!")  # <h2>
# st.subheader(body="👋 Welcome to  My Site!")  # <h3>

# st.markdown(body="Hello, _Dariush_! :kiss:")  # (_) --> Italic
# st.markdown(body="Hello, **Dariush**! :computer:")  # (**) --> Bold
# st.divider()

# st.write("Hello, Dariush! :material/thumb_up:")
# st.divider()

# st.caption(body="This is a small text!")
# st.divider()

# st.write("[Learn More](https://IranianExperts.ir)")  # Link (Anchor)
# st.divider()

# code_example: str = """
# def greet(name):
#     result = f'Hello, {name}!'
#     return result
# """

# st.code(body=code_example, language="python")
# st.divider()
# **************************************************


# **************************************************
# import streamlit as st

# st.warning(body="Warning")
# st.divider()

# st.error(body="Error")
# st.divider()

# st.info(body="Info")
# st.divider()

# st.success(body="Success")
# st.divider()

# ex = RuntimeError("This is an exception of type RuntimeError!")
# st.exception(exception=ex)
# st.divider()
# **************************************************


# **************************************************
# Display Image
# **************************************************
# import os
# import streamlit as st

# # Best Practice
# # آدرس‌دهی نسبی، نسبت به جایی که هستیم
# image_file_path: str = "./static/images/dariush_tasdighi.jpg"

# st.image(image=image_file_path)
# st.image(image=image_file_path, width=200)
# st.write("Image File Path:", image_file_path)
# st.divider()

# # Bad Practice
# # آدرس‌دهی فیزیکی
# # D:\Source_Codes\DT_Learning_Python_AI_Streamlit\static\images\dariush_tasdighi.jpg
# image_file_path = os.path.join(os.getcwd(), "static", "images", "dariush_tasdighi.jpg")

# st.image(image=image_file_path, width=200)
# st.write("Image File Path:", image_file_path)
# st.divider()
# **************************************************


# **************************************************
# import streamlit as st

# pressed: bool = st.button(label="Press Me")

# if pressed:
#     st.write("You pressed the button!")
# **************************************************


# **************************************************
# Learning: toast()
# **************************************************
# import streamlit as st

# pressed: bool = st.button(label="Press Me")

# if pressed:
#     st.toast(body="Wow! You did it...", icon="👋")
#     # st.toast(body="Wow! You did it...", icon="👋", duration="long")
#     # st.toast(body="Wow! You did it...", icon="👋", duration="short")  # Default: 'short'
#     # st.toast(body="Wow! You did it...", icon="👋", duration="infinite")

#     st.write("You pressed the button!")
# **************************************************


# **************************************************
# دو چیز باحال و هیجان‌انگیز
# **************************************************
# import streamlit as st

# button_1_pressed: bool = st.button(label="Button (1)")

# if button_1_pressed:
#     st.snow()
#     st.write("You pressed the button (1)!")

# button_2_pressed: bool = st.button(label="Button (2)")

# if button_2_pressed:
#     st.balloons()
#     st.write("You pressed the button (2)!")
# **************************************************


# **************************************************
# import streamlit as st

# name: str = st.text_input(label="Name")

# st.write(f"Hello, {name}!")
# **************************************************


# **************************************************
# Python Note!
# For Running: python .\streamlit_app.py
# **************************************************
# import os

# os.system(command="cls" if os.name == "nt" else "clear")

# name = ""  # NOK
# # name = None  # NOK
# # name = "     "  # OK
# # name = "Dariush"  # OK

# if name:
#     print("Name is not None! and is not Null String.")

# if name is not None and name != "":
#     print("Name is not None! and is not Null String.")
# **************************************************


# **************************************************
# import streamlit as st

# name: str = st.text_input(label="Name")

# # if name is not None and name != "":
# #     st.write(f"Hello, {name}!")

# if name:
#     st.write(f"Hello, {name}!")
# **************************************************


# **************************************************
# import streamlit as st

# name: str = st.text_input(label="Name")

# name = name.strip()

# # در این مثال خاص، دستور ذیل نیازی نیست
# # if name:
# #     name = name.strip()

# if name:
#     st.write(f"Hello, {name}!")
# **************************************************


# **************************************************
# یک مشکل اساسی
# **************************************************
# import streamlit as st

# number: int = 0

# pressed: bool = st.button(label="Press Me")

# if pressed:
#     number += 1
#     st.write(f"Number: {number}")
# **************************************************


# **************************************************
# حل مشکل اساسی
# **************************************************
# import streamlit as st

# # مهم: دستور ذیل صحیح نمی‌باشد
# # st.session_state.number = 0

# # Solution (1)
# # if not st.session_state.get("number"):
# #     st.session_state.number = 0

# # OR

# # Solution (2)
# if "number" not in st.session_state:
#     st.session_state.number = 0

# pressed: bool = st.button(label="Press Me")

# if pressed:
#     st.session_state.number += 1
#     st.write(f"Number: {st.session_state.number}")
# **************************************************


# **************************************************
# Create Chatbot Step by Step
# **************************************************
# import streamlit as st

# st.set_page_config(
#     page_icon="👋",
#     page_title="DT Chatbot",
# )

# st.header(body="DT Chatbot", divider="rainbow")

# # NEW
# st.chat_input(placeholder="Type your question here...")

# # NEW
# with st.chat_message(name="AI"):
#     st.write("Hello! How can I help you?")

# # NEW
# with st.chat_message(name="USER"):  # "User" OR "Human" OR "HUMAN"
#     st.write("I want to know about your products.")
# **************************************************


# **************************************************
# import streamlit as st

# # New
# AI: str = "AI"
# USER: str = "USER"

# st.set_page_config(
#     page_icon="👋",
#     page_title="DT Chatbot",
# )

# # New
# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# st.chat_input(placeholder="Type your question here...")

# with st.chat_message(name=AI):
#     st.write("Hello! How can I help you?")

# with st.chat_message(name=USER):
#     st.write("I want to know about your products.")
# **************************************************


# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"

# st.set_page_config(
#     page_icon="👋",
#     page_title="DT Chatbot",
# )

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# # New
# user_prompt: str | None = st.chat_input(placeholder="Type your question here...")

# # New
# if user_prompt:
#     with st.chat_message(name=USER):
#         st.write(user_prompt)

#     with st.chat_message(name=AI):
#         # NEW
#         assistant_answer: str = f"I don't know! {user_prompt}"
#         st.write(assistant_answer)
# **************************************************


# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"


# # New
# def chat(user_prompt: str) -> str:
#     """
#     Chat function.
#     """

#     assistant_answer: str = f"I don't know! {user_prompt}"
#     return assistant_answer


# st.set_page_config(
#     page_icon="👋",
#     page_title="DT Chatbot",
# )

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# user_prompt: str | None = st.chat_input(placeholder="Type your question here...")

# # New
# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     # NEW
#     assistant_answer: str = chat(
#         user_prompt=user_prompt,
#     )

#     with st.chat_message(name=USER):
#         st.write(user_prompt)

#     with st.chat_message(name=AI):
#         st.write(assistant_answer)
# **************************************************


# **************************************************
# We Need Chat History (Messages), But There is a Problem!
# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"


# def chat(user_prompt: str) -> str:
#     """
#     Chat function.
#     """

#     assistant_answer: str = f"I don't know! {user_prompt}"
#     return assistant_answer


# messages: list[dict] = []

# st.set_page_config(
#     page_icon="👋",
#     page_title="DT Chatbot",
# )

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# user_prompt: str | None = st.chat_input(placeholder="Type your question here...")

# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     # New
#     user_message: dict = {"role": "user", "content": user_prompt}
#     messages.append(user_message)

#     assistant_answer: str = chat(user_prompt=user_prompt)

#     # NEW
#     assistant_message: dict = {"role": "assistant", "content": assistant_answer}
#     messages.append(assistant_message)

# # NEW
# st.write(messages)
# **************************************************


# **************************************************
# Fix the previous problem with session state!
# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"


# def chat(user_prompt: str) -> str:
#     """
#     Chat function.
#     """

#     assistant_answer: str = f"I don't know! {user_prompt}"
#     return assistant_answer


# # NEW
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# st.set_page_config(
#     page_icon="👋",
#     page_title="DT Chatbot",
# )

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# user_prompt: str | None = st.chat_input(placeholder="Type your question here...")

# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     user_message: dict = {"role": "user", "content": user_prompt}
#     # New
#     st.session_state.messages.append(user_message)

#     assistant_answer: str = chat(user_prompt=user_prompt)

#     assistant_message: dict = {"role": "assistant", "content": assistant_answer}
#     # NEW
#     st.session_state.messages.append(assistant_message)

# # NEW
# st.write(st.session_state.messages)
# **************************************************


# **************************************************
# Final Code! (English)
# **************************************************
# # NEW
# import time
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"


# def chat(user_prompt: str) -> str:
#     """
#     Chat function.
#     """

#     # NEW
#     time.sleep(5)

#     assistant_answer: str = f"I don't know! {user_prompt}"
#     return assistant_answer


# if "messages" not in st.session_state:
#     st.session_state.messages = []

# st.set_page_config(
#     page_icon="👋",
#     page_title="DT Chatbot",
# )

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# user_prompt: str | None = st.chat_input(placeholder="Type your question here...")

# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     user_message: dict = {"role": "user", "content": user_prompt}
#     st.session_state.messages.append(user_message)

#     assistant_answer: str = chat(user_prompt=user_prompt)

#     assistant_message: dict = {"role": "assistant", "content": assistant_answer}
#     st.session_state.messages.append(assistant_message)

# # st.write(st.session_state.messages)

# # NEW
# for message in st.session_state.messages:
#     if message["role"] == "user":
#         with st.chat_message(name=USER):
#             st.write(message["content"])
#     elif message["role"] == "assistant":
#         with st.chat_message(name=AI):
#             st.write(message["content"])

# # for index, message in enumerate(st.session_state.messages):
# **************************************************


# **************************************************
# Final Code! (English) with Ollama
# **************************************************
# import streamlit as st

# # NEW
# import dt_ollama as ollama

# AI: str = "AI"
# USER: str = "USER"

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# st.set_page_config(
#     page_icon="👋",
#     page_title="DT Chatbot",
# )

# with st.sidebar:
#     st.subheader(body="Settings", divider="rainbow")

# st.header(body="DT Chatbot", divider="rainbow")

# user_prompt: str | None = st.chat_input(placeholder="Type your question here...")

# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     user_message: dict = {"role": "user", "content": user_prompt}
#     st.session_state.messages.append(user_message)

#     # NEW
#     assistant_answer, _, _ = ollama.chat(
#         messages=st.session_state.messages,
#     )

#     # NEW
#     if not assistant_answer:
#         st.session_state.messages.pop()
#     else:
#         assistant_message: dict = {"role": "assistant", "content": assistant_answer}
#         st.session_state.messages.append(assistant_message)

# for message in st.session_state.messages:
#     if message["role"] == "user":
#         with st.chat_message(name=USER):
#             st.write(message["content"])
#     elif message["role"] == "assistant":
#         with st.chat_message(name=AI):
#             st.write(message["content"])
# **************************************************


# **************************************************
# Final Code! (Persian)
# **************************************************
# import streamlit as st

# AI: str = "AI"
# USER: str = "USER"

# # NEW
# STREAMLIT_STYLE: str = """
# <style>
#     @import url('https://fonts.cdnfonts.com/css/iransansx');

#     html, body, p, h1, h2, h3, h4, h5, h6, input, textarea, li {
#         font-family: 'IRANSansX', tahoma !important;
#     }

#     .block-container, section, input, textarea {
#         direction: rtl;
#         text-align: justify;
#     }
# </style>
# """


# def chat(user_prompt: str) -> str:
#     """
#     Chat function.
#     """

#     # NEW
#     assistant_answer: str = f"متاسفانه من پاسخ سوال شما را نمی‌دانم! {user_prompt}"
#     return assistant_answer


# if "messages" not in st.session_state:
#     st.session_state.messages = []

# st.set_page_config(
#     page_icon="👋",
#     page_title="DT Chatbot",
# )

# # NEW
# st.markdown(
#     body=STREAMLIT_STYLE,
#     unsafe_allow_html=True,
# )

# with st.sidebar:
#     # NEW
#     st.subheader(body="تنظیمات", divider="rainbow")

# # NEW
# st.header(body="به ربات داریوش تصدیقی خوش آمدید!", divider="rainbow")

# user_prompt: str | None = st.chat_input(
#     # NEW
#     placeholder="لطفا سوال خودتان را اینجا بپرسید..."
# )

# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     user_message: dict = {"role": "user", "content": user_prompt}
#     st.session_state.messages.append(user_message)

#     assistant_answer: str = chat(user_prompt=user_prompt)

#     assistant_message: dict = {"role": "assistant", "content": assistant_answer}
#     st.session_state.messages.append(assistant_message)

# for message in st.session_state.messages:
#     if message["role"] == "user":
#         with st.chat_message(name=USER):
#             st.write(message["content"])
#     elif message["role"] == "assistant":
#         with st.chat_message(name=AI):
#             st.write(message["content"])
# **************************************************


# **************************************************
# Final Code! (Persian)
# **************************************************
# import streamlit as st
# import dt_ollama as ollama

# AI: str = "AI"
# USER: str = "USER"

# STREAMLIT_STYLE: str = """
# <style>
#     @import url('https://fonts.cdnfonts.com/css/iransansx');

#     html, body, p, h1, h2, h3, h4, h5, h6, input, textarea, li {
#         font-family: 'IRANSansX', tahoma !important;
#     }

#     .block-container, section, input, textarea {
#         direction: rtl;
#         text-align: justify;
#     }
# </style>
# """


# def get_assistant_answer(user_prompt: str) -> str:
#     """
#     Get assistant answer.
#     """

#     assistant_answer: str = f"متاسفانه من پاسخ سوال شما را نمی‌دانم! {user_prompt}"
#     return assistant_answer


# if "messages" not in st.session_state:
#     st.session_state.messages = []

# st.set_page_config(
#     page_icon="👋",
#     page_title="DT Chatbot",
# )

# st.markdown(
#     body=STREAMLIT_STYLE,
#     unsafe_allow_html=True,
# )

# with st.sidebar:
#     st.subheader(body="تنظیمات", divider="rainbow")

# st.header(body="به ربات داریوش تصدیقی خوش آمدید!", divider="rainbow")

# user_prompt: str | None = st.chat_input(
#     placeholder="لطفا سوال خودتان را اینجا بپرسید..."
# )

# if user_prompt:
#     user_prompt = user_prompt.strip()

# if user_prompt:
#     user_message: dict = {"role": "user", "content": user_prompt}
#     st.session_state.messages.append(user_message)

#     assistant_answer, _, _ = ollama.chat(
#         messages=st.session_state.messages,
#     )

#     if not assistant_answer:
#         st.session_state.messages.pop()
#     else:
#         assistant_message: dict = {"role": "assistant", "content": assistant_answer}
#         st.session_state.messages.append(assistant_message)

# for message in st.session_state.messages:
#     if message["role"] == "user":
#         with st.chat_message(name=USER):
#             st.write(message["content"])
#     elif message["role"] == "assistant":
#         with st.chat_message(name=AI):
#             st.write(message["content"])
# **************************************************


# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************


# **************************************************
# import streamlit as st
# import chatbot_constants as constants
# import chatbot_functions as functions

# functions.set_page_config()
# functions.initial_session_state()

# with st.sidebar:
#     st.subheader(body=constants.SETTINGS, divider="rainbow")

#     st.session_state.model_name = st.radio(
#         index=0,
#         options=constants.MODELS,
#         label=constants.SELECT_YOUR_MODEL,
#     ).strip()

#     st.write(constants.SELECTED_MODEL, st.session_state.model_name)
#     st.divider()

#     st.markdown(body=constants.ABOUT, unsafe_allow_html=True)
#     st.divider()

# st.header(body=constants.PAGE_HEADER, divider="rainbow")

# if not st.session_state.model_name:
#     st.error(body=constants.ERROR_YOU_DID_NOT_SPECIFY_MODEL_NAME)

# if st.session_state.model_name:
#     user_prompt: str | None = st.chat_input(
#         placeholder=constants.USER_PROMPT_PLACEHOLDER
#     )

#     if user_prompt:
#         user_prompt = user_prompt.strip()

#     if user_prompt:
#         st.session_state.messages.append({"role": "user", "content": user_prompt})
#         assistant_answer = functions.get_assistant_answer(user_prompt=user_prompt)
#         st.session_state.messages.append(
#             {"role": "assistant", "content": assistant_answer}
#         )

#     for index, message in enumerate(st.session_state.messages):
#         if message["role"] == "user":
#             with st.chat_message(name=constants.USER):
#                 st.write(message["content"])
#         elif message["role"] == "assistant":
#             with st.chat_message(name=constants.AI):
#                 st.write(message["content"])
# **************************************************

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************

# **************************************************
# import os
# import pandas as pd
# import streamlit as st

# os.system(command="cls")

# # data_frame = pd.read_csv("./data/users.csv")
# data_frame = pd.read_csv("./data/movies.csv")
# st.write(data_frame)
# **************************************************

# **************************************************
# import os
# import pandas as pd
# import streamlit as st

# os.system(command="cls")

# st.title(body="Working with Pandas!")

# data_frame = pd.DataFrame(
#     {
#         "Name": ["Alice", "Bob", "Charlie", "David"],
#         "Age": [25, 32, 37, 45],
#         "Occupation": ["Engineer", "Doctor", "Artist", "Chef"],
#     }
# )

# st.subheader(body="write()")
# st.write(data_frame)
# st.divider()

# st.subheader(body="dataframe()")
# st.dataframe(data=data_frame)
# st.divider()

# st.subheader(body="table() -> Static Table")
# st.table(data=data_frame)
# st.divider()

# st.subheader(body="data_editor() -> Editable Table")
# editable_data_frame = st.data_editor(data=data_frame)
# print(editable_data_frame)
# st.divider()

# st.subheader(body="Metrics")
# st.metric(label="Total Rows", value=len(data_frame))
# st.metric(label="Average Age", value=round(data_frame["Age"].mean(), 1))

# st.subheader(body="JSON and Dictionary")
# sample_dictionary = {
#     "name": "Dariush",
#     "age": 52,
#     "skills": {"C#", "Python", "AI", "Cyber Security"},
# }

# st.subheader(body="write()")
# st.write(sample_dictionary)

# st.subheader(body="json()")
# st.json(body=sample_dictionary)

# st.divider()
# st.write("Data:", sample_dictionary)
# **************************************************

# **************************************************
# *** Multipage App
# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.header(body="Welcome to Dariush Site!", divider="rainbow")

# st.link_button(label="About", url="/about")
# st.link_button(label="Contact", url="/contact")
# **************************************************

# **************************************************
# import os
# import yfinance as yf
# import streamlit as st

# os.system(command="cls")

# st.header(body="Dariush", divider="rainbow")

# # data_frame = yf.download(tickers="AAPL", period="1d", interval="1m")
# data_frame = yf.download(tickers="AAPL", start="2024-01-01", end="2024-01-31")

# st.table(data=data_frame)
# st.line_chart(data=data_frame.Close)
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.title(body="Dariush")

# tickers = ["ETH-USD", "BTC-USD", "TSLA"]

# dropdown = st.selectbox(label="Select a ticker", options=tickers, index=1)

# if dropdown:
#     st.write(dropdown)
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# st.title(body="Dariush")

# tickers = ["ETH-USD", "BTC-USD", "TSLA"]

# dropdown = st.multiselect(label="Select tickers", options=tickers)
# # dropdown = st.multiselect(label="Select tickers", options=tickers, default=["ETH-USD"])

# if len(dropdown) > 0:
#     # st.write(dropdown)
#     for item in dropdown:
#         st.write(item)
# **************************************************

# **************************************************
# import os
# import yfinance as yf
# import streamlit as st

# os.system(command="cls")

# st.title(body="Dariush")

# tickers = ["ETH-USD", "BTC-USD", "TSLA"]

# dropdown = st.multiselect(label="Select tickers", options=tickers)

# start_date = st.date_input(label="Start Date", value="today")
# end_date = st.date_input(label="End Date", value="today")

# if len(dropdown) > 0:
#     data_frame = yf.download(tickers=dropdown, start=start_date, end=end_date)

#     st.line_chart(data=data_frame.Close)
# **************************************************

# **************************************************
# https://www.varzesh3.com
# https://www.varzesh3.com/news
# https://search-api.varzesh3.com/v1.0/query?q=طارمی
# **************************************************
# import os
# import requests

# os.system(command="cls")

# url = "https://search-api.varzesh3.com/v1.0/query?q=طارمی"

# assistant_answer = requests.get(url=url)

# print("-" * 50)
# print("assistant_answer:", assistant_answer)
# print("-" * 50)
# print("assistant_answer.status_code:", assistant_answer.status_code)
# print("-" * 50)
# print("assistant_answer.encoding:", assistant_answer.encoding)
# print("-" * 50)
# print("assistant_answer.headers['content-type']:", assistant_answer.headers["content-type"])
# print("-" * 50)

# if assistant_answer.status_code == 200:
#     print("assistant_answer.text:")
#     print()
#     print(assistant_answer.text)  # Note: -> "
#     print("-" * 50)
#     print("assistant_answer.json():")
#     print()
#     print(assistant_answer.json())  # Note: -> '
#     print("-" * 50)

#     data = assistant_answer.json()
#     for index, item in enumerate(data["news"]):
#         row_index = index + 1

#         id = item["id"]
#         title = item["title"]
#         published_on = item["publishedOn"]

#         message = f"{row_index}: id: {id} - Published On: {published_on} - {title}"

#         print(message)
# **************************************************

# **************************************************
# import os
# import requests
# import streamlit as st

# os.system(command="cls")

# base_url = "https://search-api.varzesh3.com/v1.0/query?q="

# os.system(command="cls")

# st.title(body="Search in Varzesh3 Site")

# search = st.text_input(label="Search")

# url = f"{base_url}{search}"
# assistant_answer = requests.get(url=url)

# if assistant_answer.status_code == 200:
#     data = assistant_answer.json()
#     for index, item in enumerate(data["news"]):
#         title = item["title"]
#         short_description = item["shortDescription"]
#         persian_published_on = item["persianPublishedOn"]

#         #         message = f"""
#         # ### {title}
#         # - {short_description}
#         # - زمان انتشار: {persian_published_on}
#         # """

#         #         st.write(message)

#         st.subheader(title)
#         st.write(short_description)
#         st.success(persian_published_on)

#         st.divider()
# **************************************************

# **************************************************
# https://www.cdnfonts.com/iransansx.font
# https://www.cdnfonts.com/iranian-sans.font
# **************************************************
# import os
# import requests
# import streamlit as st

# os.system(command="cls")

# base_url = "https://search-api.varzesh3.com/v1.0/query?q="

# os.system(command="cls")

# streamlit_style = """
# <style>
#     @import url('https://fonts.cdnfonts.com/css/iransansx');

#     html, body, p, h1, h2, h3, h4, h5, h6, input, textarea {
#         font-family: 'IRANSansX', tahoma !important;
#     }

#     .block-container {
#         direction: rtl;
#         text-align: justify;
#     }
# </style>
# """

# st.markdown(body=streamlit_style, unsafe_allow_html=True)

# st.title(body="جستجو در سایت ورزش سه")

# search = st.text_input(label="جستجو")

# url = f"{base_url}{search}"
# assistant_answer = requests.get(url=url)

# if assistant_answer.status_code == 200:
#     data = assistant_answer.json()
#     for index, item in enumerate(data["news"]):
#         title = item["title"]
#         short_description = item["shortDescription"]
#         persian_published_on = item["persianPublishedOn"]

#         st.subheader(title)
#         st.write(short_description)
#         st.success(persian_published_on)

#         st.divider()
# **************************************************

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************

# **************************************************
# import streamlit as st

# st.set_page_config(page_title="Dariush Tasdighi", page_icon="👋", layout="wide")

# with st.container():
#     st.title("👋 Welcome to Dariush's Streamlit App!")
#     st.subheader("👋 Welcome to Dariush's Streamlit App!")
#     st.write("Hello, World! :wave:")
#     st.write("[Learn More >](https://IranianExperts.ir)")

# with st.container():
#     st.write("---")

#     left_column, right_column = st.columns(2)

#     with left_column:
#         st.header("Dariush Tasdighi")
#         st.write("##")
#         st.write(
#             """
# I am a student at the University of Tehran.
# I take courses in Computer Science and Mathematics.
# I teach:
# - Python
# - C++
# - C#
# - Java
# """)

#     with right_column:
#         st.header("Dariush Tasdighi")
# **************************************************

# **************************************************
# import streamlit as st

# st.header("Welcome", divider="rainbow")

# st.title("👋 Welcome to Dariush's Streamlit App!")

# st.text_input("Your name", key="name")

# # st.session_state.name

# if st.session_state.name:
#     st.markdown("### Hello, **{}**!".format(st.session_state.name))

# x = st.slider("Pick a number", 0, 10)

# if x:
#     st.markdown(f"Number is {x}!")
# **************************************************

# **************************************************
# import os
# import streamlit as st

# os.system(command="cls")

# with st.sidebar:
#     st.header("About")
#     st.write("This is my first app!")

# st.header("Welcome", divider="rainbow")

# st.title("👋 Welcome to Dariush's Streamlit App!")

# st.text_input("Your name", key="name")

# # st.session_state.name

# if st.session_state.name:
#     st.markdown("### Hello, **{}**!".format(st.session_state.name))

# x = st.slider("Pick a number", 0, 10)

# if x:
#     st.markdown(f"Number is {x}!")
# **************************************************

# **************************************************
# **************************************************
# **************************************************
# **************************************************
# **************************************************
