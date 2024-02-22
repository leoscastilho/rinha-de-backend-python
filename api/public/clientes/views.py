from operator import attrgetter

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from api.database import get_session
from api.public.clientes.crud import (
    create_cliente,
    delete_cliente,
    read_cliente,
    read_clientes,
    update_cliente,
)
from api.public.clientes.models import ClientesCreate, ClientesRead, ClientesUpdate
from api.public.extrato.models import Extrato
from api.public.extrato.services import generate_extrato
from api.public.transacoes.models import TransacaoRequest, TransacaoResponse
from api.public.transacoes.services import process_transacao

router = APIRouter()


@router.post("", response_model=ClientesRead)
def create_a_cliente(cliente: ClientesCreate, db: Session = Depends(get_session)):
    return create_cliente(cliente=cliente, db=db)


@router.get("", response_model=list[ClientesRead])
def get_clientes(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        db: Session = Depends(get_session),
):
    return read_clientes(offset=offset, limit=limit, db=db)


@router.get("/{cliente_id}/extrato", response_model=Extrato)
def get_cliente_extrato(cliente_id: int, db: Session = Depends(get_session)):
    cliente = read_cliente(cliente_id=cliente_id, db=db)
    return generate_extrato(cliente)


@router.post("/{cliente_id}/transacoes", response_model=TransacaoResponse)
def post_process_transacao(cliente_id: int, transacaoRequest: TransacaoRequest, db: Session = Depends(get_session)):
    cliente = read_cliente(cliente_id=cliente_id, db=db)
    response = process_transacao(transacaoRequest, cliente, db)
    return response


@router.patch("/{cliente_id}", response_model=ClientesRead)
def update_a_cliente(cliente_id: int, cliente: ClientesUpdate, db: Session = Depends(get_session)):
    return update_cliente(cliente_id=cliente_id, cliente=cliente, db=db)


@router.delete("/{cliente_id}")
def delete_a_cliente(cliente_id: int, db: Session = Depends(get_session)):
    return delete_cliente(cliente_id=cliente_id, db=db)
