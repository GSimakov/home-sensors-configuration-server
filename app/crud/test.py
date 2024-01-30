from app.crud.base import CRUDBase
from app.schemas.test_schema import IUserCreate, IUserUpdate
from app.models.test import User
from app.core.connections.db.session import async_session


class CRUDUser(CRUDBase[User, IUserCreate, IUserUpdate]):
    pass


user = CRUDUser(model=User, session=async_session)
