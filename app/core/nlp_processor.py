# app/core/nlp_processor.py
import spacy
import os

nlp = spacy.load('pt_core_news_sm')

def extract_text(file_path):
    text = ""
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        from PyPDF2 import PdfReader
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    elif extension in [".docx", ".doc"]:
        import docx
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif extension == ".txt":
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = ""
    return text

def processar_curriculo(file_path):
    text = extract_text(file_path)
    doc = nlp(text)

    habilidades = []
    experiencias = []
    formacoes = []

    # Exemplo simplificado de extração
    for ent in doc.ents:
        if ent.label_ == "PER":
            # Possível nome ou pessoa mencionada
            pass
        elif ent.label_ == "ORG":
            experiencias.append(ent.text)
        elif ent.label_ == "EDUC":
            formacoes.append(ent.text)
        elif ent.label_ == "MISC":
            habilidades.append(ent.text)

    return {
        'habilidades': habilidades,
        'experiencias': experiencias,
        'formacoes': formacoes
    }
