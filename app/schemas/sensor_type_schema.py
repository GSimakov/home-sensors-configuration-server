from uuid import UUID
from app import models


class ISensorTypeCreate(models.BaseSensorType):
    pass


class ISensorTypeUpdate(models.SensorTypeUpdate):
    pass


class ISensorTypeRead(models.BaseSensorType):
    id: UUID

