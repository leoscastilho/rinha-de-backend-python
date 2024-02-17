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
from api.public.clientes.models import ClienteCreate, ClienteRead, ClienteUpdate

router = APIRouter()


@router.post("", response_model=ClienteRead)
def create_a_cliente(cliente: ClienteCreate, db: Session = Depends(get_session)):
    return create_cliente(cliente=cliente, db=db)


@router.get("", response_model=list[ClienteRead])
def get_clientes(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    db: Session = Depends(get_session),
):
    return read_clientes(offset=offset, limit=limit, db=db)


@router.get("/{cliente_id}", response_model=ClienteRead)
def get_a_hero(cliente_id: int, db: Session = Depends(get_session)):
    return read_cliente(cliente_id=cliente_id, db=db)


@router.patch("/{cliente_id}", response_model=ClienteRead)
def update_a_cliente(cliente_id: int, cliente: ClienteUpdate, db: Session = Depends(get_session)):
    return update_cliente(cliente_id=cliente_id, cliente=cliente, db=db)


@router.delete("/{cliente_id}")
def delete_a_cliente(cliente_id: int, db: Session = Depends(get_session)):
    return delete_cliente(cliente_id=cliente_id, db=db)