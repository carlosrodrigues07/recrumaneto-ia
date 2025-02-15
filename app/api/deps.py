# app/api/deps.py
from typing import Generator
from app.config import SessionLocal

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
