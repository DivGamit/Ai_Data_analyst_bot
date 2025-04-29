import pandas as pd
from PyPDF2 import PdfReader
from docx import Document

def handle_uploads(files):
    docs, dataframes = [], []
    for file in files:
        if file.type == "application/pdf":
            reader = PdfReader(file)
            text = "\n".join(page.extract_text() or '' for page in reader.pages)
            docs.append(text)
        elif file.type == "text/csv":
            df = pd.read_csv(file)
            dataframes.append(df)
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(file)
            text = "\n".join(p.text for p in doc.paragraphs)
            docs.append(text)
    return docs, dataframes
