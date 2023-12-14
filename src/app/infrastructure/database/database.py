from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.application.config.config import Config


class Base(DeclarativeBase):
    pass


def create_async_session_maker(config: Config):
    database_url = 'postgresql+asyncpg://%s:%s@%s:5432/%s' % (
        config.POSTGRES_USER,
        config.POSTGRES_PASSWORD,
        config.POSTGRES_HOST,
        config.POSTGRES_DB,
    )
    engine = create_async_engine(
        database_url,
    )
    return async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )


async def get_async_session(async_session_maker: async_sessionmaker) -> AsyncGenerator:
    async with async_session_maker() as session:
        yield session
