from uuid import UUID
from app import models


__all__ = ['IDASCreate', 'IDASUpdate', 'IDASRead']

base_model = models.BaseDataAcquisitionSystem
update_model = models.DataAcquisitionSystemUpdate


class IDASCreate(base_model):
    pass


class IDASUpdate(update_model):
    pass


class IDASRead(base_model):
    id: UUID

