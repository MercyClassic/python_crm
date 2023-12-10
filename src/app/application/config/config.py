from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=('.env', '../.env'))
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str

    POSTGRES_USER_TEST: str
    POSTGRES_PASSWORD_TEST: str
    POSTGRES_HOST_TEST: str
    POSTGRES_DB_TEST: str

    ROOT_DIR: str = '%s' % Path(__file__).parent.parent.parent


def get_config() -> Config:
    return Config()
