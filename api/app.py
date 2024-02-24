import json
import streamlit as st
import ast
from dotenv import load_dotenv

from collections import defaultdict
from functions.file_reader import read_pdf
from functions.text_chunk import get_text_chunks
from functions.vectorizer import get_vectorizers
from functions.conversation_chain import get_conversation_chain
from functions.question_handler import handle_user_input
import streamlit.components.v1 as components

def on_press():
    st.session_state.edited_question = st.session_state.widget3
    st.session_state.edited_question = ""
def on_enter():
    st.session_state.question = st.session_state.widget
    st.session_state.question = ""

def one_question():
    st.session_state.user_question = st.session_state.widget2
    st.session_state.user_question = ""

def main():
    """Driver function to run the codebase
    """
    load_dotenv()
    if  "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "question" not in st.session_state:
        st.session_state.question = ""
    if "generated_questions" not in st.session_state and "flag" not in st.session_state:
        st.session_state.generated_questions = None
        st.session_state.flag = True

    # just some ornamenting codes
    st.set_page_config(
        page_title="Efficient Data Conversation",
        page_icon=":green_book:",
        layout="wide"
    )

    st.header("Efficient Data Conversation: :green_book:")
    st.subheader("Your PDF documents")

    # utility to upload pdf files
    pdf_docs = st.file_uploader(
        "Upload your PDF documents",
        accept_multiple_files=True
    )
    # if the button is pressed then the reader will
    # start to read pages of contents from the pdfs
    if st.button("Process") and pdf_docs:
        # most of the codes will go to backend process
        # after integrating fastapi
        # i = 0
        with st.spinner("Processing your documents"):
            # reading raw text from pdfs
            raw_text = read_pdf(pdf_docs=pdf_docs)
            # chunk texts into small pieces
            text_chunks = get_text_chunks(raw_text=raw_text)
            # print(text_chunks)
            # get vectorstores
            vectorstores = get_vectorizers(chunked_texts=text_chunks)
            # conversation chain construction
            st.session_state.generated_questions = get_conversation_chain(vectorstores)

            #generate sets of questions from the given texts in the given language
            handle_user_input(user_question="Generate 5 Questions in Dutch from the Given Text",
                                        session_variable=st.session_state.generated_questions)
            if st.session_state.flag:
                st.session_state.conversation = st.session_state.generated_questions
                st.session_state.batch_conversation = st.session_state.generated_questions
                st.session_state.flag = False

    if user_question := st.text_input("Any queries about the PDFs? : ", key="widget2", on_change=one_question):
        #to avoid focusing issue in streamlit
        #===================================
        components.html(
                    """
                <script>
                const doc = window.parent.document;
                const inputs = doc.querySelectorAll('input');

                inputs.forEach(input => {
                input.addEventListener('focusout', function(event) {
                    event.stopPropagation();
                    event.preventDefault();
                    console.log("lost focus")
                });
                });question

                </script>""",
                    height=0,
                    width=0,
        )
        #===================================

        if st.session_state.conversation:
            response = handle_user_input(user_question=user_question,
                        session_variable=st.session_state.conversation)
            # ----------------------
            if response[-1].content:
                # ----------------------
                st.write("Law Chat's Response:")
                st.write(response[-1].content)
                st.write("Database record for this question")
                st.write("Chat History")
                st.write(response)
        else:
            st.write("Please press the process button first after uploading the PDFs")

if __name__=="__main__":
    main()