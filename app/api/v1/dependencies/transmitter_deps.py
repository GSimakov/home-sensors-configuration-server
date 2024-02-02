from uuid import UUID
from fastapi import Query, Body, Path
from typing_extensions import Annotated

from app import crud
from app import models
from app.utils.exceptions import IdNotFoundException

__all__ = ['get_transmitter_by_id_from_path', 'get_transmitter_by_id_from_query']

model = models.Transmitter
id_param_description = 'The UUID id of transmitter'


async def get(id: UUID) -> model:
    response = await crud.transmitter.get(id=id)
    if not response:
        raise IdNotFoundException(model=model, id=id)
    return response


async def get_transmitter_by_id_from_path(
        id: Annotated[UUID, Path(description=id_param_description)]
) -> model:
    return await get(id=id)


async def get_transmitter_by_id_from_query(
        id: Annotated[UUID, Query(description=id_param_description)]
) -> model:
    return await get(id=id)
