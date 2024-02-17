import os
import secrets
from typing import Literal

from pydantic_settings import BaseSettings

from api.config.dev import config as dev_config
from api.config.prod import config as prod_config
from api.env import config as envs

environment = os.environ['PYTHON_ENV'] or 'development'
environment_config = None
if environment == 'development':
    environment_config = dev_config
if environment == 'production':
    environment_config = prod_config

def chain_configs(*config_items):
    for it in config_items:
        for element in it:
            value = element[1]
                if value is not None:
                    yield element

config = dict(chain_configs(environment_config.items, envs.items()))

class Settings(BaseSettings):
    PROJECT_NAME: str = f"Rinha de Backend API - {os.getenv('ENV', 'development').capitalize()}"
    DESCRIPTION: str = "Rinha de backend utilizando FastAPI + SQLModel production-ready API"
    ENV: Literal["development", "staging", "production"] = "development"
    VERSION: str = "0.1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DATABASE_URI: str = dev_config.da
    API_USERNAME: str = "svc_test"
    API_PASSWORD: str = "superstrongpassword"

    class Config:
        case_sensitive = True


settings = Settings()


class TestSettings(Settings):
    class Config:
        case_sensitive = True


test_settings = TestSettings()
