from pydantic import BaseModel

from uuid import UUID
from app import models

__all__ = ['IBoardCreate', 'IBoardUpdate', 'IBoardRead']

base_model = models.BaseBoard
update_model = models.BoardUpdate


class IBoardCreate(base_model):
    pass


class IBoardUpdate(update_model):
    pass


class IBoardRead(base_model):
    id: UUID


class IBoardShortRead(BaseModel):
    id: UUID
    name: str

