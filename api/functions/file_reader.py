import os
import sys
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

import os
import re
import fitz
from collections import defaultdict
# from unstructured.partition.pdf import partition_pdf
from langchain_community.document_loaders import UnstructuredPDFLoader, UnstructuredFileIOLoader

def preprocess_text(text: str) -> str:
    """preprocessing text for some simple
    pattern basis

    Args:
        text (str): text in string

    Returns:
        str: preprocessed text in string
    """
    # pattern = re.compile(r"[^\w\s\%\.]")
    text = " ".join(text.splitlines())
    # text = pattern.sub(" ", text)
    return text

# def read_pdf(pdf_docs) -> str:
#     """reading texts from multiple pdf files.

#     Args:
#         pdf_docs (object): pdf files
#     Returns:
#         text (str): text with characters in string
#     """
#     text_dict = defaultdict(None)
#     table_list = defaultdict(None)
#     for i, pdf in enumerate(pdf_docs):
#         if type(pdf)==str:
#             pdf_reader_object = fitz.open(pdf)
#         else:
#             pdf_reader_object = fitz.open(stream=pdf.read(), filetype="pdf")
#         text_dict[f"doc_no_{i+1}"] = ""
#         for j, page in enumerate(pdf_reader_object):
#             print(f"Page Number: {j+1}")
#             text = page.get_text("dict", sort=True)
#             for block in text["blocks"]:
#                 # print(k)
#                 if block["type"] == 0:
#                     # print(block_list["lines"])
#                     for lines in enumerate(block["lines"]):
#                         for k, span in enumerate(lines["spans"]):
#                             print(span)
#                     # print()
#                     # k+=1
#             # print(len(text["blocks"]))#[0].keys())
#             # text = text["blocks"][0]
#             # print(text)

#             # if text[j][5] !=0:
#             #     continue
#                 # print(text[j][4])
#                 # print(text[j][5])

#             # print("===========")
#             # print(text["blocks"][17].keys())
#             # print(text["blocks"][17]["lines"][0].keys())
#             # print(text["blocks"][17]["lines"][0]["spans"][0].keys())
#             # print(text["blocks"][17]["lines"][0]["spans"][0]["font"])
#             # for t in text.items():
#             # print(text["blocks"])
#                 # print(t["blocks"][17]["lines"][0]["spans"][0]["font"])
#             print("===========")
#             # break
#             # if text[j][5] !=0:
#             #     print(text[j][4])
#             #     print(text[j][5])
#             # break
#             # tabs = page.find_tables(horizontal_strategy="text")
#             # for tab in tabs:
#             #     # print(tab.extract())
#             #     # print(dir(tab.to_pandas()))
#             #     tab.to_pandas(dropna=True).to_dict()
#             #     print("===================")
#             #     # break
#             # text = text[j][4]
#             # text = preprocess_text(text=text)
#             # text_dict[f"doc_no_{i+1}"]+=" "+text
#             if j>1:
#                 break
#     text_list = list(text_dict.values())[0].split()
#     # print(text_list)
#     # print(len(text_list))
#     # text_list[0].split()
#     for i, text in enumerate(text_list):
#         if text is not None:
#             # print(text)
#             text_list[i] = str(text).strip()
#     # text_dict["doc_no_1"] = " ".join(text_list)
#     return " ".join(text_list)

def preprocess_text(text: str) -> str:
    """preprocessing text for some simple
    pattern basis

    Args:
        text (str): text in string

    Returns:
        str: preprocessed text in string
    """
    # pattern = re.compile(r"[^\w\s%-]")
    text = " ".join(text.splitlines())
    # text = pattern.sub("", text)
    return text

# def read_pdf(pdf_docs) -> str:
#     """reading texts from multiple pdf files.

#     Args:
#         pdf_docs (object): pdf files
#     Returns:
#         text (str): text with characters in string
#     """
#     text_dict = defaultdict(None)
#     table_list = defaultdict(None)
#     for i, pdf in enumerate(pdf_docs):
#         if type(pdf)==str:
#             pdf_reader_object = fitz.open(pdf)
#         else:
#             pdf_reader_object = fitz.open(stream=pdf.read(), filetype="pdf")
#         text_dict[f"doc_no_{i+1}"] = ""
#         for j, page in enumerate(pdf_reader_object):
#             text = page.get_text(sort=True)
#             # tabs = page.find_tables(horizontal_strategy="text")
#             # for tab in tabs:
#             #     # print(tab.extract())
#             #     # print(dir(tab.to_pandas()))
#             #     tab.to_pandas(dropna=True).to_dict()
#             #     print("===================")
#             #     # break
#             text = preprocess_text(text=text)
#             text_dict[f"doc_no_{i+1}"]+=" "+text
#             # if j>2:
#             #     break
#     text_list = list(text_dict.values())[0].split()
#     # print(text_list)
#     # print(len(text_list))
#     # text_list[0].split()
#     for i, text in enumerate(text_list):
#         if text is not None:
#             # print(text)
#             text_list[i] = str(text).strip()
#     # text_dict["doc_no_1"] = " ".join(text_list)
#     return " ".join(text_list)

def read_pdf(pdf_docs) -> str:
    for pdf in pdf_docs:
        print(pdf)
        print(type(pdf))
        if isinstance(pdf, str):
            data_file = UnstructuredPDFLoader(pdf)
        else:
            data_file = UnstructuredFileIOLoader(pdf)
        docs = data_file.load()
    text = preprocess_text(docs[0].page_content)
    return text

if __name__=="__main__":
    # print(" ".join(read_pdf("./test/ed3bookfeb3_2024.pdf")))
    file_list = [
        os.path.join(f"./test/t/{pdf_file}")
        for _, pdf_file in enumerate(os.listdir("./test/t/"))
    ]
    # print(file_list)

    # print(read_pdf(file_list))
    read_pdf(file_list)