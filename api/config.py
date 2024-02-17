import os
import secrets
from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = f"Rinha de Backend API - {os.getenv('ENV', 'development').capitalize()}"
    DESCRIPTION: str = "Rinha de backend utilizando FastAPI + SQLModel production-ready API"
    ENV: Literal["development", "staging", "production"] = "development"
    VERSION: str = "0.1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DATABASE_URI: str = "postgresql://admin:123@db:5432/rinha"
    API_USERNAME: str = "svc_test"
    API_PASSWORD: str = "superstrongpassword"

    class Config:
        case_sensitive = True


class DevelopmentSettings(Settings):
    DATABASE_URI: str = "postgresql://admin:123@localhost:5432/rinha"

    class Config:
        case_sensitive = True


environment = os.environ.get('PYTHON_ENV', 'development')
if environment == 'development':
    settings = DevelopmentSettings()
if environment == 'production':
    settings = Settings()
