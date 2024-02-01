from uuid import UUID
from app import models


class ISensorCreate(models.BaseSensor):
    pass


class ISensorUpdate(models.SensorUpdate):
    pass


class ISensorRead(models.BaseSensor):
    id: UUID

