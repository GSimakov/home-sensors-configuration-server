import datetime
from uuid import UUID
from app import models

__all__ = ['IMeasurementTypeCreate', 'IMeasurementTypeUpdate', 'IMeasurementTypeRead']

base_model = models.BaseMeasurementType
update_model = models.MeasurementTypeUpdate


class IMeasurementTypeCreate(base_model):
    pass


class IMeasurementTypeUpdate(update_model):
    pass


class IMeasurementTypeRead(base_model):
    id: UUID
    created_at: datetime.datetime

