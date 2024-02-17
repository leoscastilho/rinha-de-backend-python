from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from api.database import get_session
from api.public.clientes.models import Cliente, ClienteCreate, ClienteUpdate


def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_session)):
    cliente_to_db = Cliente.model_validate(cliente)
    db.add(cliente_to_db)
    db.commit()
    db.refresh(cliente_to_db)
    return cliente_to_db


def read_clientes(offset: int = 0, limit: int = 20, db: Session = Depends(get_session)):
    clientes = db.exec(select(Cliente).offset(offset).limit(limit)).all()
    return clientes


def read_cliente(cliente_id: int, db: Session = Depends(get_session)):
    cliente = db.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente not found with id: {cliente_id}",
        )
    return cliente


def update_cliente(cliente_id: int, cliente: ClienteUpdate, db: Session = Depends(get_session)):
    cliente_to_update = db.get(Cliente, cliente_id)
    if not cliente_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente not found with id: {cliente_id}",
        )

    #TODO: updates to cliente

    db.add(cliente_to_update)
    db.commit()
    db.refresh(cliente_to_update)
    return cliente_to_update


def delete_cliente(cliente_id: int, db: Session = Depends(get_session)):
    cliente = db.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente not found with id: {cliente_id}",
        )

    db.delete(cliente)
    db.commit()
    return {"ok": True}
