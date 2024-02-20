from fastapi import APIRouter, Depends

from api.auth import authent
from api.public.health import views as health
from api.public.clientes import views as clientes
from api.public.transacoes import views as transacoes


api = APIRouter()


api.include_router(
    health.router,
    prefix="/health",
    tags=["Health"],
)
api.include_router(
    clientes.router,
    prefix="/clientes",
    tags=["Clientes"],
    # dependencies=[Depends(authent)],
)
api.include_router(
    transacoes.router,
    prefix="/transacoes",
    tags=["Transacoes"],
    # dependencies=[Depends(authent)],
)
