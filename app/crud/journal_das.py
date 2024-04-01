from fastapi import HTTPException
from typing import Any, Generic, TypeVar
from uuid import UUID
from fastapi_pagination.ext.async_sqlalchemy import paginate
from fastapi_pagination import Params, Page
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlmodel import SQLModel, select, func
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.sql.expression import Select
from sqlalchemy import exc, desc, asc

from app.utils.session import session_manager
from app.crud.base import CRUDBase
from app import schemas
from app import models

model = models.JournalDAS
update_schema = None
create_schema = schemas.IJournalDASCreate


class CRUDJournalDAS(CRUDBase[model, create_schema, update_schema]):

    @session_manager
    async def get_multi_paginated(
            self,
            session: AsyncSession,
            params: Params | None = Params(),
    ) -> Page[model]:
        query = select(self.model)
        return await paginate(session, query, params)


journal_das = CRUDJournalDAS(model=model)
