from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship


class TransacoesBase(SQLModel):
    valor: int
    tipo: str
    descricao: str
    realizada_em: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,  # Incremental
                "cliente_id": 1,
                "valor": 10,
                "tipo": "c",
                "descricao": "descricao",
                "realizada_em": "2024-01-17T02:34:38.543030Z"  # Default NOW
            }
        }


class Transacoes(TransacoesBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    cliente_id: Optional[int] = Field(default=None, foreign_key="clientes.id")
    clientes: Optional["Clientes"] = Relationship(back_populates="transacoes")


class TransacaoCreate(TransacoesBase):
    cliente_id: int
    valor: int
    tipo: str
    descricao: str
    realizada_em: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "cliente_id": 1,
                "valor": 10,
                "tipo": "c",
                "descricao": "descricao",
                "realizada_em": "2024-01-17T02:34:38.543030Z"
            }
        }


class TransacaoRead(TransacoesBase):
    cliente_id: int
    valor: int | None = None
    tipo: str | None = None
    descricao: str | None = None
    realizada_em: datetime | None = None
    clientes: list | None = None


class TransacaoRequest(BaseModel):
    valor: int | None = None
    tipo: str | None = None
    descricao: str | None = None


class TransacaoResponse(BaseModel):
    limite: int | None = None
    saldo: int | None = None
