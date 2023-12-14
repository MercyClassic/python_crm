from functools import partial

from fastapi import FastAPI

from app.application.config.config import Config
from app.infrastructure.database.database import (
    create_async_session_maker,
    get_async_session,
)
from app.main.di.dependencies.stub import get_session_stub


def init_dependencies(app: FastAPI, config: Config):
    async_session_maker = create_async_session_maker(config)

    app.dependency_overrides[get_session_stub] = partial(
        get_async_session,
        async_session_maker,
    )
