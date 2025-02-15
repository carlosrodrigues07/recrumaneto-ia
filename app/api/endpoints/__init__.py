# app/api/endpoints/__init__.py

from app.api.endpoints.candidatos import router as candidatos_router
from app.api.endpoints.vagas import router as vagas_router

__all__ = ["candidatos_router", "vagas_router"]
