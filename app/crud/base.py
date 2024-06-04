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


DefaultModelType = TypeVar("DefaultModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[DefaultModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[DefaultModelType]):
        self.model = model

    @session_manager
    async def get(
            self,
            session: AsyncSession,
            id: UUID | str
    ) -> DefaultModelType | None:
        query = select(self.model).where(self.model.id == id)
        response = await session.execute(query)
        return response.scalar_one_or_none()

    @session_manager
    async def get_by_ids(
        self,
        session: AsyncSession,
        list_ids: list[UUID | str],
    ) -> list[DefaultModelType] | None:
        response = await session.execute(
            select(self.model).where(self.model.id.in_(list_ids))
        )
        return response.scalars().all()

    @session_manager
    async def get_count_wrapped(
        self,
        session: AsyncSession
    ) -> DefaultModelType | None:
        response = await session.execute(
            select(func.count()).select_from(select(self.model).subquery())
        )
        return response.scalar_one()

    @session_manager
    async def get_multi(
        self,
        session: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[DefaultModelType]:
        query = select(self.model).offset(skip).limit(limit).order_by(self.model.id)
        response = await session.execute(query)
        return response.scalars().all()

    @session_manager
    async def get_multi_paginated(
        self,
        session: AsyncSession,
        params: Params | None = Params(),
    ) -> Page[DefaultModelType]:
        query = select(self.model).order_by(desc(self.model.created_at))
        return await paginate(session, query, params)

    @session_manager
    async def create(
        self,
        session: AsyncSession,
        obj_in: CreateSchemaType | DefaultModelType,
        created_by_id: UUID | str | None = None,
    ) -> DefaultModelType:
        db_obj = self.model.from_orm(obj_in)  # type: ignore

        if created_by_id:
            db_obj.created_by_id = created_by_id

        try:
            session.add(db_obj)
            await session.commit()
        except exc.IntegrityError:
            await session.rollback()
            raise HTTPException(
                status_code=409,
                detail="Resource already exists",
            )
        await session.refresh(db_obj)
        return db_obj

    @session_manager
    async def update(
        self,
        session: AsyncSession,
        obj_current: DefaultModelType,
        obj_new: UpdateSchemaType | dict[str, Any] | DefaultModelType,
    ) -> DefaultModelType:
        obj_data = jsonable_encoder(obj_current)

        if isinstance(obj_new, dict):
            update_data = obj_new
        else:
            update_data = obj_new.dict(
                exclude_unset=True
            )  # This tells Pydantic to not include the values that were not sent
        for field in obj_data:
            if field in update_data:
                setattr(obj_current, field, update_data[field])

        session.add(obj_current)
        await session.commit()
        await session.refresh(obj_current)
        return obj_current

    @session_manager
    async def remove(
            self,
            session: AsyncSession,
            id: UUID | str
    ) -> DefaultModelType:
        response = await session.execute(
            select(self.model).where(self.model.id == id)
        )
        obj = response.scalar_one()
        await session.delete(obj)
        await session.commit()
        return obj

#todo передать все операции сессии session_manager, кроме выполнения запроса