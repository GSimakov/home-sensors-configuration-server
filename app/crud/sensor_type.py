from app.crud.base import CRUDBase
from app import schemas
from app import models


class CRUDSensorType(CRUDBase[models.SensorType, schemas.ISensorTypeCreate, schemas.ISensorTypeUpdate]):
    pass


sensor_type = CRUDSensorType(model=models.SensorType)
