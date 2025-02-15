# app/api/endpoints/vagas.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api import deps
from app.schemas.vagas import VagaCreate, Vaga
from app.crud.crud_vagas import crud_vaga

router = APIRouter()

@router.post("/", response_model=Vaga)
def criar_vaga(
    vaga_in: VagaCreate,
    db: Session = Depends(deps.get_db)
):
    vaga = crud_vaga.create(db=db, vaga=vaga_in)
    return vaga

@router.get("/", response_model=List[Vaga])
def listar_vagas(
    db: Session = Depends(deps.get_db)
):
    vagas = crud_vaga.get_all(db=db)
    return vagas
