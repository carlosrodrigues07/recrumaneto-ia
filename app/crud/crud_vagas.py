# app/crud/crud_vaga.py

from sqlalchemy.orm import Session
from app.models.vagas import Vaga
from app.schemas.vagas import VagaCreate, VagaUpdate

class CRUDVaga:
    def get(self, db: Session, id: int):
        return db.query(Vaga).filter(Vaga.id == id).first()

    def get_all(self, db: Session):
        return db.query(Vaga).all()

    def create(self, db: Session, vaga: VagaCreate):
        db_obj = Vaga(
            titulo=vaga.titulo,
            descricao=vaga.descricao,
            requisitos=vaga.requisitos,
            habilidades_desejadas=vaga.habilidades_desejadas
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

crud_vaga = CRUDVaga()
