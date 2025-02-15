# app/models/vaga.py
from sqlalchemy import Column, Integer, String, JSON
from app.models.base_class import Base

class Vaga(Base):
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    requisitos = Column(JSON)
    habilidades_desejadas = Column(JSON)
