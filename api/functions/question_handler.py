import os
import sys
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

def handle_user_input(user_question: str, session_variable: object) -> str:
    """analysing the user question and acquiring answer
    from the model

    Args:
        user_question (str): question in plain text string
        session_variable (object): streamlit object / normal variable
                                    containing the context of the chat

    Returns:
        str: response from the model
    """
    return session_variable({"question": user_question})["chat_history"]
