from sqlmodel import Field, SQLModel, Relationship

from api.public.transacoes.models import Transacoes

class ClientesBase(SQLModel):
    nome: str
    limite: int | None = None
    saldo: int | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nome": "Clark Kent",
                "limite": 1000,
                "saldo": 500
            }
        }


class Clientes(ClientesBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transacoes: list["Transacoes"] = Relationship(back_populates="clientes")


class ClientesCreate(ClientesBase):
    pass


class ClientesRead(ClientesBase):
    id: int
    nome: str | None = None
    limite: int | None = None
    saldo: int | None = None
    transacoes: list[Transacoes] = None


class ClientesUpdate(ClientesBase):
    nome: str | None = None
    limite: int | None = None
    saldo: int | None = None
    transacoes: list[Transacoes] = None

    class Config:
        json_schema_extra = {
            "example": {
                "nome": "Clark Kent",
                "limite": 1000,
                "saldo": 500
            }
        }
