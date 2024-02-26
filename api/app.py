import streamlit as st
from dotenv import load_dotenv

from functions.file_reader import read_pdf
from functions.text_chunk import get_text_chunks
from functions.vectorizer import get_vectorizers
from functions.conversation_chain import get_conversation_chain
from functions.question_handler import handle_user_input
import streamlit.components.v1 as components

def single_question():
    st.session_state.user_question = st.session_state.widget1
    st.session_state.user_question = ""

def main():
    """Driver function to run the codebase
    """
    load_dotenv()
    if  "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "question" not in st.session_state:
        st.session_state.question = ""
    if "state_counter" not in st.session_state:
        st.session_state.state_counter = -1
    if "vectorstores" not in st.session_state:
        st.session_state.vectorstores = None

    # just some ornamenting codes
    st.set_page_config(
        page_title="Efficient Data Conversation",
        page_icon=":cat2:",
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
        with st.spinner("Processing your documents"):
            # reading raw text from pdfs
            raw_text = read_pdf(pdf_docs=pdf_docs)
            # chunk texts into small pieces
            text_chunks = get_text_chunks(raw_text=raw_text)
            # print(text_chunks)
            # get vectorstores
            vectorstores = get_vectorizers(chunked_texts=text_chunks)
            st.session_state.vectorstores = vectorstores
            # conversation chain construction
            st.session_state.conversation = get_conversation_chain(vectorstores)
            # print(st.session_state.conversation)

    if user_question := st.text_input("Any queries about the PDFs? : ", key="widget1", on_change=single_question):
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
            st.session_state.state_counter+=1
            response = handle_user_input(user_question=user_question,
                        session_variable=st.session_state.conversation)
            # if st.session_state.state_counter>2:
            #     print("Resetting State")
            #     st.session_state.conversation = get_conversation_chain(st.session_state.vectorstores)
            #     st.session_state.state_counter = 0
            # ----------------------
            if response[-1].content:
                # ----------------------
                st.write("Law Chat's Response:")
                st.write(response[-1].content)
                st.sidebar.header("Records")
                st.sidebar.write("Chat History")
                st.sidebar.write(response)
        else:
            st.write("Please press the process button first after uploading the PDFs")

if __name__=="__main__":
    main()