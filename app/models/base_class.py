# app/models/base_class.py
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: any
    __name__: str

    # Gera automaticamente o nome da tabela a partir do nome da classe
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
