from app.core.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine

asyncpg_engine = create_async_engine(
    settings.ASYNC_DATABASE_URL,
    echo=False,
    future=True,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=15,
)