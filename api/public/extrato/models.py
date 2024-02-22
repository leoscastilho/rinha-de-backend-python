from pydantic import BaseModel
from datetime import datetime

now = datetime.now()


class TransacaoExtratoRead(BaseModel):
    valor: int | None = None
    tipo: str | None = None
    descricao: str | None = None
    realizada_em: datetime | None = None


class Saldo(BaseModel):
    total: int | None = None
    data_extrato: str = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    limite: int | None = None


class Extrato(BaseModel):
    saldo: Saldo | None = None
    ultimas_transacoes: list[TransacaoExtratoRead] | None = None
