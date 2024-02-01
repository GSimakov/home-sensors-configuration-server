from app.crud.base import CRUDBase
from app import schemas
from app import models


class CRUDMeasurementType(
    CRUDBase[
        models.MeasurementType,
        schemas.IMeasurementTypeCreate,
        schemas.IMeasurementTypeUpdate
    ]
):
    pass


measurement_type = CRUDMeasurementType(model=models.MeasurementType)
