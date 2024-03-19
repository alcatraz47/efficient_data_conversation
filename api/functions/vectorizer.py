import os
import sys
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

from config import settings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS, Qdrant
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

def get_vectorizers(chunked_texts: list) -> object:
    """converts chunk of texts into vectors of embeddings

    Args:
        chunked_texts (list): list of texts
    Returns:
        (object): faiss vectorstore object
    """
    if settings.use_gpu == 1:
        embedding_creator = HuggingFaceEmbeddings(
            model_name = settings.embedding_model_path,#settings.embedding_model_path,
            model_kwargs={"device": "cuda"},
            encode_kwargs={"normalize_embeddings": False}
        )
    else:
        embedding_creator = HuggingFaceEmbeddings(
            model_name = settings.embedding_model_path,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": False}
        )
    # return FAISS.from_texts(texts=chunked_texts,
    #                         embedding=embedding_creator)
    # embedding_creator = model
    # embedding_creator.encode_kwargs = {"normalize_embeddings": False}
    vectorstore_retriever = Qdrant.from_texts(
        texts=chunked_texts,
        embedding=embedding_creator,
        location=":memory:"
    ).as_retriever(search_type="mmr", search_kwargs = {"k": 5})

    keyword_retriever = BM25Retriever.from_texts(
        texts=chunked_texts,
    )
    keyword_retriever.k = 3

    ensemble_retrievers = EnsembleRetriever(
        retrievers = [vectorstore_retriever, keyword_retriever],
        weights = [0.3, 0.7]
    )

    return ensemble_retrievers
