from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from api.database import get_session
from api.public.transacoes.crud import (
    create_transacao,
    delete_transacao,
    read_transacao,
    read_transacoes
)
from api.public.transacoes.models import TransacaoCreate, TransacaoRead

router = APIRouter()


@router.post("", response_model=TransacaoRead)
def create_a_transacao(transacao: TransacaoCreate, db: Session = Depends(get_session)):
    return create_transacao(transacao=transacao, db=db)
