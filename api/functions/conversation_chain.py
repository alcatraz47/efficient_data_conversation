import os
import sys
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

from config import settings
from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def get_conversation_chain(vectorstore: object) -> object:
    """conversation chain with context

    Args:
        vectorstore (object): vector of embeddings

    Returns:
        object: return the object of the chat conversation
    """
    if settings.use_gpu == 1:
        language_model = Ollama(
            base_url=settings.llm_model_host,
            model=settings.llm_model_name,
            temperature=settings.temperature,
            num_gpu=settings.use_gpu,
            num_ctx=settings.tokens_per_chunk,
            num_predict=settings.tokens_per_chunk,
            # top_k=20,
            # top_p=0.1,
            timeout=settings.timeout
        )
    else:
        language_model = Ollama(
            base_url=settings.llm_model_host,
            model=settings.llm_model_name,
            temperature=settings.temperature,
            num_gpu=0,
            num_thread=settings.num_threds,
            num_ctx=settings.tokens_per_chunk,
            num_predict=settings.tokens_per_chunk,
            # top_k=20,
            # top_p=0.1,
            timeout=settings.timeout
        )
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    return ConversationalRetrievalChain.from_llm(
        llm=language_model,
        retriever=vectorstore.as_retriever(search_type="mmr", search_kwargs = {"k": 5}),
        memory=memory
    )