from sqlmodel import Field, SQLModel


class ClienteBase(SQLModel):
    id: int
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


class Cliente(ClienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ClienteCreate(ClienteBase):
    pass


class ClienteRead(ClienteBase):
    id: int
    nome: str | None = None
    limite: int | None = None
    saldo: int | None = None


class ClienteUpdate(ClienteBase):
    nome: str | None = None
    limite: int | None = None
    saldo: int | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "nome": "Clark Kent",
                "limite": 1000,
                "saldo": 500
            }
        }
