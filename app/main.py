from fastapi import FastAPI
from fastapi_async_sqlalchemy import SQLAlchemyMiddleware
from fastapi_pagination import add_pagination
from starlette.middleware.cors import CORSMiddleware

from app.core.main_events import create_start_app_handler, create_stop_app_handler
from app.core.settings import settings

app = FastAPI(**settings.fastapi_kwargs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SQLAlchemyMiddleware,
                   db_url=settings.ASYNC_DATABASE_URL,
                   engine_args={
                       "echo": False,
                       "pool_pre_ping": True,
                       "pool_size": settings.DB_POOL_SIZE,
                       "max_overflow": 64,
                   })

app.add_event_handler(
    event_type="startup",
    func=create_start_app_handler(app)
)
app.add_event_handler(
    event_type="shutdown",
    func=create_stop_app_handler(app),
)

add_pagination(app)
