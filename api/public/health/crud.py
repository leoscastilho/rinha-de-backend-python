from fastapi import Depends
from sqlmodel import Session, text

from api.config.config import settings
from api.database import get_session
from api.public.health.models import Health, Stats, Status
from api.public.clientes.crud import read_clientes
from api.utils.logger import logger_config

logger = logger_config(__name__)


def get_health(db: Session) -> Health:
    db_status = health_db(db=db)
    logger.info("%s.get_health.db_status: %s", __name__, db_status)
    return Health(app_status=Status.OK, db_status=db_status, environment=settings.ENV)


def get_stats(db: Session) -> Stats:
    stats = Stats(clientes=count_from_db("clientes", db))
    logger.info("%sget_stats: %s", __name__, stats)
    return stats


def count_from_db(table: str, db: Session = Depends(get_session)):
    clientes = db.exec(text(f"SELECT COUNT(id) FROM {table};")).one_or_none()
    return clientes[0] if clientes else 0


def health_db(db: Session = Depends(get_session)) -> Status:
    try:
        db.exec(text(f"SELECT COUNT(id) FROM clientes;")).one_or_none()
        return Status.OK
    except Exception as e:
        logger.exception(e)

    return Status.KO
