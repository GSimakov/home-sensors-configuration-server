from app import crud, models, schemas

crud_repo = crud.das
model = models.DAS
update_schema = schemas.IDASUpdate
create_schema = schemas.IDASCreate


async def registration(hardware_id: str, addr: str):

    current = await crud_repo.get_by_hardware_id(hardware_id=hardware_id)

    if current:
        if current.address == addr:
            return 'Already registered'

        else:
            update = update_schema(address=addr)
            updated_das = await crud_repo.update(obj_current=current, obj_new=update)
            return 'Registration details updated'

    new_das = create_schema(hardware_id=hardware_id, address=addr)
    await crud_repo.create(obj_in=new_das)
    return 'Successfully registered'
