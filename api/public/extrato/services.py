from operator import attrgetter

from api.public.clientes.models import Clientes
from api.public.extrato.models import TransacaoExtratoRead, Saldo, Extrato


def generate_extrato(cliente: Clientes):
    sorted_transacoes = []
    if len(cliente.transacoes) > 0:
        sorted_transacoes = sorted(cliente.transacoes, key=attrgetter("realizada_em"), reverse=True)[:10]
    ultimas_transacoes = [
        TransacaoExtratoRead(valor=obj.valor, tipo=obj.tipo, descricao=obj.descricao, realizada_em=obj.realizada_em) for
        obj in sorted_transacoes]
    saldo = Saldo(total=cliente.saldo, limite=cliente.limite)
    extrato = Extrato(saldo=saldo, ultimas_transacoes=ultimas_transacoes)
    return extrato
