# app/schemas/vaga.py

from typing import List, Optional
from pydantic import BaseModel

class VagaBase(BaseModel):
    titulo: str
    descricao: str

class VagaCreate(VagaBase):
    requisitos: Optional[List[str]] = []
    habilidades_desejadas: Optional[List[str]] = []

class VagaUpdate(VagaBase):
    requisitos: Optional[List[str]] = []
    habilidades_desejadas: Optional[List[str]] = []

class VagaInDBBase(VagaBase):
    id: int

    class Config:
        from_attributes = True  # Para compatibilidade com Pydantic 2.0

class Vaga(VagaInDBBase):
    requisitos: Optional[List[str]] = []
    habilidades_desejadas: Optional[List[str]] = []
