from fastapi import HTTPException, status
from sqlmodel import Session

from api.public.clientes.crud import update_cliente
from api.public.clientes.models import ClientesUpdate
from api.public.transacoes.crud import create_transacao
from api.public.transacoes.models import TransacaoRequest, TransacaoCreate
from datetime import datetime

now = datetime.now()


def validate_transacao(transacao: TransacaoRequest):
    if transacao.valor <= 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Transaction with negative value: {transacao.valor}",
        )
    if transacao.tipo not in ["c", "d"]:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Transaction with invalid tipo: {transacao.tipo}"
        )
    return


def validate_saldo(transacao: TransacaoRequest, cliente: ClientesUpdate):
    if (cliente.limite + cliente.saldo) < transacao.valor:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Transaction with valor: {transacao.valor} greater than available saldo: {cliente.limite + cliente.saldo}"
        )
    return


def process_transacao(transacao: TransacaoRequest, cliente: ClientesUpdate, db: Session):
    validate_transacao(transacao)
    if transacao.tipo is "d":
        validate_saldo(transacao, cliente)
        cliente.saldo -= transacao.valor
    else:
        cliente.saldo += transacao.valor
    updated_cliente = update_cliente(cliente_id=cliente.id, cliente=cliente, db=db)
    created_transacao = create_transacao(transacao=TransacaoCreate(cliente_id=updated_cliente.id,
                                                                   valor=transacao.valor,
                                                                   tipo=transacao.tipo,
                                                                   descricao=transacao.descricao,
                                                                   realizada_em=now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                                                                   ),
                                         db=db)
    return {
        "limite": updated_cliente.limite,
        "saldo": updated_cliente.saldo
    }
