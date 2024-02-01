from app.crud.base import CRUDBase
from app import schemas
from app import models


class CRUDSensor(CRUDBase[models.Sensor, schemas.ISensorCreate, schemas.ISensorUpdate]):
    pass


sensor = CRUDSensor(model=models.Sensor)
