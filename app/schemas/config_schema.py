from uuid import UUID
from app import models


__all__ = ['IConfigCreate', 'IConfigUpdate', 'IConfigRead']

base_model = models.Config
update_model = models.ConfigUpdate


class IConfigCreate(base_model):
    pass


class IConfigUpdate(update_model):
    pass


class IConfigRead(base_model):
    id: UUID

