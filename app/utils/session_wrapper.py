from app.core.connections.db.session import async_session


def session_wrapper(func):

    async def wrap(*args, **kwargs):
        async with async_session() as session:
            response = await func(session=session, *args, **kwargs)
            await session.close()
        return response

    return wrap


# def session_wrapper_wrong(func):
#                             # при использовании контекстного менеджера сессия всегда закрфвается
#     async def wrap(*args, **kwargs):
#         # async with async_session() as session:
#         session = async_session()
#         response = await func(session=session, *args, **kwargs)
#             # await session.close()
#         return response
#
#     return wrap
#