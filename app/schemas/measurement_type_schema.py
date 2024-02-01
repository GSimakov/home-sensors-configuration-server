from uuid import UUID
from app import models


class IMeasurementTypeCreate(models.BaseMeasurementType):
    pass


class IMeasurementTypeUpdate(models.MeasurementTypeUpdate):
    pass


class IMeasurementTypeRead(models.BaseMeasurementType):
    id: UUID

