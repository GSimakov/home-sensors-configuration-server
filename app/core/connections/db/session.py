from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from .engine import asyncpg_engine

connect_args = {"check_same_thread": False}


async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=asyncpg_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)