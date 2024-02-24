import os
import sys
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

from config import settings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def get_vectorizers(chunked_texts: list) -> object:
    """converts chunk of texts into vectors of embeddings

    Args:
        chunked_texts (list): list of texts
    Returns:
        (object): faiss vectorstore object
    """
    embedding_creator = HuggingFaceEmbeddings(
        model_name = settings.embedding_model_path,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": False}
    )
    return FAISS.from_texts(texts=chunked_texts,
                            embedding=embedding_creator)
