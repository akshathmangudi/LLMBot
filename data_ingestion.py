from dotenv import load_dotenv
from PyPDF2 import PdfReader


def get_pdf_text(pdf_document):
    text = ""
    for pdf in pdf_document:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
