from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from api.database import get_session
from api.public.transacoes.models import Transacoes, TransacaoCreate


def create_transacao(transacao: TransacaoCreate, db: Session = Depends(get_session)):
    transacao_to_db = Transacoes.model_validate(transacao)
    db.add(transacao_to_db)
    db.commit()
    db.refresh(transacao_to_db)
    return transacao_to_db


def read_transacoes(offset: int = 0, limit: int = 20, db: Session = Depends(get_session)):
    transacoes = db.exec(select(Transacoes).offset(offset).limit(limit)).all()
    return transacoes


def read_transacao(transacao_id: int, db: Session = Depends(get_session)):
    transacao = db.get(Transacoes, transacao_id)
    if not transacao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transacao not found with id: {transacao_id}",
        )
    return transacao


def delete_transacao(transacao_id: int, db: Session = Depends(get_session)):
    transacao = db.get(Transacoes, transacao_id)
    if not transacao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente not found with id: {transacao_id}",
        )

    db.delete(transacao)
    db.commit()
    return {"ok": True}
