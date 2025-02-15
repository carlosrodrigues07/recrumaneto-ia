# app/utils/file_handler.py
import shutil
import os
from uuid import uuid4

UPLOAD_DIR = "uploads/"

def save_file(upload_file):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    filename = f"{uuid4()}_{upload_file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path
