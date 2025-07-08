import os
from django.conf import settings
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

# 1. Extract PDF Text
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

def get_chunks_from_pdf():
    # Load and prepare PDF text
    pdf_path = os.path.join(settings.BASE_DIR, 'general_safety_rules.pdf')
    pdf_text = extract_text_from_pdf(pdf_path)

    # Split the text into chunks
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(pdf_text)

    return chunks
