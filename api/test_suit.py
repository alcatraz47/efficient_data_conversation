import os
import sys
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

from functions.file_reader import read_pdf
from functions.vectorizer import get_vectorizers
from functions.text_chunk import get_text_chunks

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from sentence_transformers import SentenceTransformer

if __name__=="__main__":
    # tokenizer = AutoTokenizer.from_pretrained("api/lang_models/robbert-2023-dutch-large")
    # model = AutoModelForSequenceClassification.from_pretrained("api/lang_models/robbert-2023-dutch-large")
    # model_pipeline = pipeline(task="feature-extraction", model=model, tokenizer=tokenizer)

    file_list = [
        os.path.join(f"api/functions/test/t/{pdf_file}")
        for _, pdf_file in enumerate(os.listdir("api/functions/test/t/"))
    ]
    # print(file_list)

    raw_texts = read_pdf(file_list)
    # print(raw_texts)

    # print("========================")

    # raw_texts = [
    #     "Basquetball is a great sport.",
    #     "Fly me to the moon is one of my favourite songs.",
    #     "The Celtics are my favourite team.",
    #     "This is a document about the Boston Celtics",
    #     "I simply love going to the movies",
    #     "The Boston Celtics won the game by 20 points",
    #     "This is just a random text.",
    #     "Elden Ring is one of the best games in the last 15 years.",
    #     "L. Kornet is one of the best Celtics players.",
    #     "Larry Bird was an iconic NBA player.",
    # ]

    chunked_texts = get_text_chunks(raw_text=raw_texts)
    # print(chunked_texts)
    # print(raw_texts)

    # retriever = get_vectorizers(chunked_texts=raw_texts.split(". ")).as_retriever(search_kwargs={"k":5})#chunked_texts
    retriever = get_vectorizers(chunked_texts=chunked_texts)
    question = "Most accurate model described here"#"Name of the authors"#"Email ids of the authors"#"What can you tell me about a team?"#
    # print(dir(vectorizer))


    docs = retriever.get_relevant_documents(question)
    print(docs)