from app.core.connections.db.session import async_session


def session_manager(func):

    async def wrap(*args, **kwargs):
        async with async_session() as session:
            response = await func(session=session, *args, **kwargs)
            await session.close()
        return response

    return wrap


