from app.core.connections.db.session import AsyncSession


def session_manager(func):
    async def wrap(*args, **kwargs):
        async with AsyncSession() as session:
            response = await func(session=session, *args, **kwargs)
            await session.close()
        return response

    return wrap


