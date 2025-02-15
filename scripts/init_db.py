# scripts/init_db.py
from app.config import engine
from app.models.base_class import Base
from app.models.candidato import Candidato
from app.models.vagas import Vaga

print("Criando as tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso.")
