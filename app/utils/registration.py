from app import crud, models, schemas

crud_das = crud.das
crud_journal = crud.journal_das

update_schema_das = schemas.IDASUpdate
create_schema_das = schemas.IDASCreate

create_schema_journal = schemas.IJournalDASCreate


async def registration(hardware_id: str, addr: str):

    event = 'Registration Event'

    current = await crud_das.get_by_hardware_id(hardware_id=hardware_id)

    if current:
        if current.address == addr:
            status = 'Already authenticated'
            journal_event = create_schema_journal(event=event, status=status, DAS_id=current.id)
            await crud_journal.create(obj_in=journal_event)
            return 0

        else:
            update = update_schema_das(address=addr)
            updated_das = await crud_das.update(obj_current=current, obj_new=update)
            status = 'Authentication details updated' #todo naming
            journal_event = create_schema_journal(event=event, status=status, DAS_id=updated_das.id)
            await crud_journal.create(obj_in=journal_event)
            return 0

    new_das = create_schema_das(hardware_id=hardware_id, address=addr)
    registered_das = await crud_das.create(obj_in=new_das)

    status = 'Successfully registered'
    journal_event = create_schema_journal(event=event, status=status, DAS_id=registered_das.id)
    await crud_journal.create(obj_in=journal_event)
    return 0
