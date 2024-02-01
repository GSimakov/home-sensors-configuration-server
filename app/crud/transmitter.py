from app.crud.base import CRUDBase
from app import schemas
from app import models


class CRUDTransmitter(
    CRUDBase[
        models.Transmitter,
        schemas.ITransmitterCreate,
        schemas.ITransmitterUpdate
    ]
):
    pass


transmitter = CRUDTransmitter(model=models.MeasurementType)
