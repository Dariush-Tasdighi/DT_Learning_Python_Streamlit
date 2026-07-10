"""
Dariush Tasdighi Constants Module
"""

from typing import Final
import dt_utility as utility

PAGE_TITLE: Final[str] = "DT Chatbot!"
HEADER_SETTINGS: Final[str] = "Settings"
USER_QUESTION: Final[str] = "Enter your prompt"

if __name__ == "__main__":
    utility.display_just_one_error_message(
        message=utility.ERROR_MESSAGE_MODULE_IS_NOT_EXECUTED_DIRECTLY,
    )
