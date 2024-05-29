from pydantic import BaseModel

from uuid import UUID
from app import models

__all__ = ['ISensorCreate', 'ISensorUpdate', 'ISensorRead']

base_model = models.BaseSensor
update_model = models.SensorUpdate


class ISensorCreate(base_model):
    pass


class ISensorUpdate(update_model):
    pass


class ISensorRead(base_model):
    id: UUID


class ISensorShortRead(BaseModel):
    id: UUID
    name: str
