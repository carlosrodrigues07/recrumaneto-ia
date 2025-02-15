# app/models/candidato.py
from sqlalchemy import Column, Integer, String, JSON
from app.models.base_class import Base

class Candidato(Base):
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefone = Column(String, nullable=True)
    habilidades = Column(JSON)
    experiencias = Column(JSON)
    formacoes = Column(JSON)
    curriculo = Column(String)  # Caminho para o arquivo do currículo
