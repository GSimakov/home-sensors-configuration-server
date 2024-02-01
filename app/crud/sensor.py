from app.crud.base import CRUDBase
from app.schemas.sensor_schema import ISensorCreate, ISensorUpdate
from app.models.sensor import Sensor
from app.core.connections.db.session import async_session


class CRUDSensor(CRUDBase[Sensor, ISensorCreate, ISensorUpdate]):
    pass


sensor = CRUDSensor(model=Sensor, session=async_session)
