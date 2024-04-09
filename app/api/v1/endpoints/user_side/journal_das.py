from fastapi import APIRouter, Depends
from fastapi_pagination import Params

from app import schemas
from app import models
from app import crud

from app.schemas.response_schema import (
    create_response,
    IGetResponsePaginated,
)

router = APIRouter()

obj_in_message = 'DAS journal'

model = models.JournalDAS
read_schema = schemas.IJournalDASRead
create_schema = schemas.IJournalDASCreate

crud_repo = crud.journal_das


@router.get("/list")
async def read_journal_list(
        params: Params = Depends(),
) -> IGetResponsePaginated[read_schema]:
    """
    Gets a paginated list of DAS events
    """
    response = await crud_repo.get_multi_paginated(params=params)
    print(response)
    return create_response(data=response)
