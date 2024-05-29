from uuid import UUID

from app import models
from app import crud
from app.utils.exceptions import NameExistException, IdNotFoundException

__all__ = ['das_name_is_taken', 'das_is_exist']

crud_repo = crud.das
model = models.das


async def das_name_is_taken(name: str) -> None:
    obj = await crud_repo.get_by_name(name=name)
    if obj:
        raise NameExistException(model=model, name=name)


async def das_is_exist(id: UUID) -> None:
    obj = await crud_repo.get(id=id)
    if not obj:
        raise IdNotFoundException(model=model, id=id)
