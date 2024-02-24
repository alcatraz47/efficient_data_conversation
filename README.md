Efficient Data Conversation

Chat with your data while uploading a pdf file and using a local LLM.

Language Support:
    1. English
    2. Others are loading...

Key Dependencies:

    1. [Ollama](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image) with or without GPU
    2. Sentence-transformers
    3. Langchain

The models in use:

    1. Sentence Embedding: [multi-qa-distilbert-cos-v1](https://huggingface.co/sentence-transformers/multi-qa-distilbert-cos-v1)
    2. LLM: Mistral-7b, instruct-v0.2-q2_K via [Ollama serve](https://ollama.com/library/mistral/tags)

```
    To store models, inside the "api" directory open a directory named "lang_models"
```
![plot](./directory.png)