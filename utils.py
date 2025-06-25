import os
from docx import Document
from pdfminer.high_level import extract_text as extract_pdf_text

def extract_text_from_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    elif ext == '.pdf':
        try:
            return extract_pdf_text(filepath)
        except Exception as e:
            return f"Error reading PDF: {str(e)}"
    elif ext == '.docx':
        try:
            doc = Document(filepath)
            return '\n'.join([para.text for para in doc.paragraphs])
        except Exception as e:
            return f"Error reading DOCX: {str(e)}"
    else:
        return "Unsupported file format."
