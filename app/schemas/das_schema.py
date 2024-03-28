from uuid import UUID
from app import models


class IDASCreate(models.BaseDataAcquisitionSystem):
    pass


class IDASUpdate(models.DataAcquisitionSystemUpdate):
    pass


class IDASRead(models.BaseDataAcquisitionSystem):
    id: UUID

