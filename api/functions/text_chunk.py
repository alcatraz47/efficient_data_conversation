import os
import sys
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

from config import settings
from langchain.text_splitter import SentenceTransformersTokenTextSplitter

def get_text_chunks(raw_text: str) -> list:
    """chunks texts into subgroups to avoid overloading
    the model and get tokenizer error

    Args:
        raw_text (str): string containing whole text from pdfs

    Returns:
        list: list of texts in string format
    """
    text_splitter = SentenceTransformersTokenTextSplitter(
        model_name=settings.embedding_model_path,#settings.embedding_model_path,
        tokens_per_chunk=settings.tokens_per_chunk,
        chunk_overlap=0
    )
    return text_splitter.split_text(raw_text)
