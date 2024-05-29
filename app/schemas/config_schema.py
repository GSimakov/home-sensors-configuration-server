from pydantic import BaseModel

from uuid import UUID
from app import models


__all__ = ['IConfigCreate', 'IConfigUpdate', 'IConfigRead']

base_model = models.BaseConfig
update_model = models.ConfigUpdate


class IConfigCreate(base_model):
    pass


class IConfigUpdate(update_model):
    pass


class IConfigRead(base_model):
    id: UUID


class IConfigShortRead(BaseModel):
    id: UUID
    name: str

