import os
import sys
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

from config import settings
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationalRetrievalChain

def get_conversation_chain(vectorstore: object) -> object:
    """conversation chain with context

    Args:
        vectorstore (object): vector of embeddings

    Returns:
        object: return the object of the chat conversation
    """
    language_model = ChatOllama(
        base_url=settings.llm_model_host,
        model=settings.llm_model_name,
        temperature=0.2,
        num_gpu=0
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