# app/main.py

from fastapi import FastAPI
from app.api.endpoints import candidatos_router, vagas_router

app = FastAPI(title="Sistema de Recrutamento Inteligente")

app.include_router(candidatos_router, prefix="/candidatos", tags=["candidatos"])
app.include_router(vagas_router, prefix="/vagas", tags=["vagas"])

# Nova rota para o caminho raiz
@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo ao Sistema de Recrutamento Inteligente"}

