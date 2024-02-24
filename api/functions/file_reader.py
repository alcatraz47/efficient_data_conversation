import os
import sys
import traceback
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)

import os
import re
import fitz
from collections import defaultdict

def preprocess_text(text: str) -> str:
    """preprocessing text for some simple
    pattern basis

    Args:
        text (str): text in string

    Returns:
        str: preprocessed text in string
    """
    pattern = re.compile(r"[^\w\s]")
    text = " ".join(text.splitlines())
    text = pattern.sub("", text)
    return text

def read_pdf(pdf_docs) -> str:
    """reading texts from multiple pdf files.

    Args:
        pdf_docs (object): pdf files
    Returns:
        text (str): text with characters in string
    """
    text_dict = defaultdict(None)
    for i, pdf in enumerate(pdf_docs):
        pdf_reader_object = fitz.open(stream=pdf.read(), filetype="pdf")
        text_dict[f"doc_no_{i+1}"] = ""
        for _, page in enumerate(pdf_reader_object):
            text = page.get_text(sort=True)
            text = preprocess_text(text=text)
            text_dict[f"doc_no_{i+1}"]+=" "+text
            # if _>2:
            #     break
        # tabs = page.find_tables()
        # if tabs.tables:
        #     try:
        #         print(tabs.tables)
        #         print(tabs[0].extract()[0])
        #         print()
        #     except IndexError as ie:
        #         print(ie.print_stack())
        #         pass
    return text_dict

# if __name__=="__main__":
#     # print(" ".join(read_pdf("./test/ed3bookfeb3_2024.pdf")))
#     file_list = [
#         os.path.join(f"./test/{pdf_file}")
#         for _, pdf_file in enumerate(os.listdir("./test/"))
#     ]
#     print(file_list)

#     print(read_pdf(file_list))