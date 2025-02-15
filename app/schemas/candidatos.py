# app/schemas/candidato.py
from typing import List, Optional
from pydantic import BaseModel

class CandidatoBase(BaseModel):
    nome: str
    email: str
    telefone: Optional[str] = None

class CandidatoCreate(CandidatoBase):
    pass  # Adicione os campos necessários para criação

class CandidatoUpdate(CandidatoBase):
    habilidades: Optional[List[str]] = []
    experiencias: Optional[List[str]] = []
    formacoes: Optional[List[str]] = []

class CandidatoInDBBase(CandidatoBase):
    id: int

    class Config:
        orm_mode = True

class Candidato(CandidatoInDBBase):
    habilidades: Optional[List[str]] = []
    experiencias: Optional[List[str]] = []
    formacoes: Optional[List[str]] = []
    curriculo: Optional[str] = None
