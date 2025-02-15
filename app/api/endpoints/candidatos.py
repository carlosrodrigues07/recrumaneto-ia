# app/api/endpoints/candidatos.py

from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.candidatos import CandidatoCreate, Candidato
from app.crud.crud_candidato import crud_candidato
from app.utils.file_handler import save_file
from app.core.nlp_processor import processar_curriculo

router = APIRouter()

@router.post("/", response_model=Candidato)
async def criar_candidato(
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(None),
    arquivo: UploadFile = File(...),
    db: Session = Depends(deps.get_db)
):
    caminho_arquivo = save_file(arquivo)
    dados_extraidos = processar_curriculo(caminho_arquivo)

    candidato_in = CandidatoCreate(
        nome=nome,
        email=email,
        telefone=telefone,
        habilidades=dados_extraidos['habilidades'],
        experiencias=dados_extraidos['experiencias'],
        formacoes=dados_extraidos['formacoes'],
        curriculo=caminho_arquivo
    )
    candidato = crud_candidato.create(db=db, candidato=candidato_in)
    return candidato
