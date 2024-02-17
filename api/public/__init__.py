from fastapi import APIRouter, Depends

from api.auth import authent
from api.public.health import views as health
from api.public.clientes import views as clientes

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
    dependencies=[Depends(authent)],
)
