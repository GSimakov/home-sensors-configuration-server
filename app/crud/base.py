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
from sqlalchemy import exc

from app.utils.session_wrapper import session_wrapper


DefaultModelType = TypeVar("DefaultModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[DefaultModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, session: AsyncSession, model: type[DefaultModelType]):
        self.model = model
        self.session = session

    async def get(
        self, *, id: UUID | str
    ) -> DefaultModelType | None:
        query = select(self.model).where(self.model.id == id)
        response = await self.session.execute(query)
        return response.scalar_one_or_none()

    async def get_by_ids(
        self,
        *,
        list_ids: list[UUID | str],
    ) -> list[DefaultModelType] | None:
        response = await self.session.execute(
            select(self.model).where(self.model.id.in_(list_ids))
        )
        return response.scalars().all()

    # async def get_count(
    #     self
    # ) -> DefaultModelType | None:
    #
    #     async with self.session() as session:
    #         response = await session.execute(
    #             select(func.count()).select_from(select(self.model).subquery())
    #         )
    #     return response.scalar_one()

    @session_wrapper
    async def get_count_wrapped(
        self,
        session: AsyncSession
    ) -> DefaultModelType | None:
        response = await session.execute(
            select(func.count()).select_from(select(self.model).subquery())
        )
        return response.scalar_one()

    async def get_multi(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> list[DefaultModelType]:
        query = select(self.model).offset(skip).limit(limit).order_by(self.model.id)
        response = await self.session.execute(query)
        return response.scalars().all()

    async def get_multi_paginated(
        self,
        *,
        params: Params | None = Params(),
    ) -> Page[DefaultModelType]:
        query = select(self.model)
        return await paginate(self.session, query, params)

    async def create(
        self,
        *,
        obj_in: CreateSchemaType | DefaultModelType,
        created_by_id: UUID | str | None = None,
    ) -> DefaultModelType:
        db_obj = self.model.from_orm(obj_in)  # type: ignore

        if created_by_id:
            db_obj.created_by_id = created_by_id

        try:
            self.session.add(db_obj)
            await self.session.commit()
        except exc.IntegrityError:
            await self.session.rollback()
            raise HTTPException(
                status_code=409,
                detail="Resource already exists",
            )
        await self.session.refresh(db_obj)
        return db_obj

    async def update(
        self,
        *,
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

        self.session.add(obj_current)
        await self.session.commit()
        await self.session.refresh(obj_current)
        return obj_current

    async def remove(
        self, *, id: UUID | str
    ) -> DefaultModelType:
        response = await self.session.execute(
            select(self.model).where(self.model.id == id)
        )
        obj = response.scalar_one()
        await self.session.delete(obj)
        await self.session.commit()
        return obj





# class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
#     def __init__(self, session: AsyncSession, model: type[ModelType]):
#         self.model = model
#         self.session = session
#
#     async def get(
#         self, *, id: UUID | str
#     ) -> ModelType | None:
#         query = select(self.model).where(self.model.id == id)
#         response = await self.session.execute(query)
#         return response.scalar_one_or_none()
#
#     async def get_by_name(
#             self,
#             *,
#             name: str,
#     ) -> ModelType | None:
#         responce = await self.session.execute(
#             select(self.model).where(self.model.name == name))
#         return responce.scalar_one_or_none()
#
#     async def get_by_ids(
#         self,
#         *,
#         list_ids: list[UUID | str],
#     ) -> list[ModelType] | None:
#         response = await self.session.execute(
#             select(self.model).where(self.model.id.in_(list_ids))
#         )
#         return response.scalars().all()
#
#     async def get_count(
#         self
#     ) -> ModelType | None:
#
#         async with self.session() as session:
#             response = await session.execute(
#                 select(func.count()).select_from(select(self.model).subquery())
#             )
#         return response.scalar_one()
#
#     async def get_multi(
#         self,
#         *,
#         skip: int = 0,
#         limit: int = 100,
#         query: T | Select[T] | None = None,
#     ) -> list[ModelType]:
#         if query is None:
#             query = select(self.model).offset(skip).limit(limit).order_by(self.model.id)
#         response = await self.session.execute(query)
#         return response.scalars().all()
#
#     async def get_multi_paginated(
#         self,
#         *,
#         params: Params | None = Params(),
#         query: T | Select[T] | None = None,
#     ) -> Page[ModelType]:
#         if query is None:
#             query = select(self.model)
#         return await paginate(self.session, query, params)
#
#     async def create(
#         self,
#         *,
#         obj_in: CreateSchemaType | ModelType,
#         created_by_id: UUID | str | None = None,
#     ) -> ModelType:
#         db_obj = self.model.from_orm(obj_in)  # type: ignore
#
#         if created_by_id:
#             db_obj.created_by_id = created_by_id
#
#         try:
#             self.session.add(db_obj)
#             await self.session.commit()
#         except exc.IntegrityError:
#             await self.session.rollback()
#             raise HTTPException(
#                 status_code=409,
#                 detail="Resource already exists",
#             )
#         await self.session.refresh(db_obj)
#         return db_obj
#
#     async def update(
#         self,
#         *,
#         obj_current: ModelType,
#         obj_new: UpdateSchemaType | dict[str, Any] | ModelType,
#     ) -> ModelType:
#         obj_data = jsonable_encoder(obj_current)
#
#         if isinstance(obj_new, dict):
#             update_data = obj_new
#         else:
#             update_data = obj_new.dict(
#                 exclude_unset=True
#             )  # This tells Pydantic to not include the values that were not sent
#         for field in obj_data:
#             if field in update_data:
#                 setattr(obj_current, field, update_data[field])
#
#         self.session.add(obj_current)
#         await self.session.commit()
#         await self.session.refresh(obj_current)
#         return obj_current
#
#     async def remove(
#         self, *, id: UUID | str
#     ) -> ModelType:
#         response = await self.session.execute(
#             select(self.model).where(self.model.id == id)
#         )
#         obj = response.scalar_one()
#         await self.session.delete(obj)
#         await self.session.commit()
#         return obj