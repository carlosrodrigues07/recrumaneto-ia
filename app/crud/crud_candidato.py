# app/crud/crud_candidato.py
from sqlalchemy.orm import Session
from app.models.candidato import Candidato
from app.schemas.candidatos import CandidatoCreate, CandidatoUpdate

class CRUDCandidato:
    def get(self, db: Session, id: int):
        return db.query(Candidato).filter(Candidato.id == id).first()

    def create(self, db: Session, candidato: CandidatoCreate):
        db_obj = Candidato(
            nome=candidato.nome,
            email=candidato.email,
            telefone=candidato.telefone
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: Candidato, updates: CandidatoUpdate):
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

crud_candidato = CRUDCandidato()
