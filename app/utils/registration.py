import uuid

from app import crud, models, schemas

crud_board = crud.board
crud_das = crud.das
crud_journal = crud.journal_das

update_schema_das = schemas.IDASUpdate
create_schema_das = schemas.IDASCreate
update_schema_board = schemas.IBoardUpdate
create_schema_board = schemas.IBoardCreate

create_schema_journal = schemas.IJournalDASCreate


async def register(hardware_id: str, addr: str):

    # event = 'Registration Event'

    current = await crud_board.get_by_hardware_id(hardware_id=hardware_id)

    if current:
        if current.address == addr:
            # status = 'Already authenticated'
            # journal_event = create_schema_journal(event=event, status=status, DAS_id=current.id)
            # await crud_journal.create(obj_in=journal_event)
            return 0

        else:
            update = update_schema_board(address=addr)
            updated_board = await crud_board.update(obj_current=current, obj_new=update)
            # status = 'Authentication details updated' #todo naming
            # journal_event = create_schema_journal(event=event, status=status, DAS_id=updated_das.id)
            # await crud_journal.create(obj_in=journal_event)
            return 0

    new_board = create_schema_board(hardware_id=hardware_id, address=addr)
    created_board = await crud_board.create(obj_in=new_board)

    new_das = create_schema_das(board_id=created_board.id)
    registered_das = await crud_das.create(obj_in=new_das)

    # status = 'Successfully registered'
    # journal_event = create_schema_journal(event=event, status=status, DAS_id=registered_das.id)
    # await crud_journal.create(obj_in=journal_event)

    return 0


# async def unregister(hardware_id: str):
#
#     event = 'Registration Event'
#
#     current = await crud_das.get_by_hardware_id(hardware_id=hardware_id)
#
#     print(current)
#
#     if current:
#         await crud_das.remove(id=current.id)
#         das_id = current.id
#         status = 'DAS removed'
#
#     else:
#         status = 'DAS with hardware id "{}" not found'.format(hardware_id)
#         print(status)
#         das_id = None
#
#     journal_event = create_schema_journal(event=event, status=status, DAS_id=uuid.uuid4())
#     await crud_journal.create(obj_in=journal_event)
#     return 0