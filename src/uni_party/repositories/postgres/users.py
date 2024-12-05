from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from uni_party.entities.user import User
from uni_party.repositories.postgres import pg_session
from uni_party.repositories.postgres.pg_tables.users import users_table


async def pg_get_user_by_tg_id(tg_id: int):
    async with pg_session() as session:
        query = select(users_table).where(users_table.c.tg_id == tg_id)
        result = await session.execute(query)
        user_row = result.fetchone()

    if user_row:
        return User(
            id=user_row.id,
            tg_id=user_row.tg_id,
            username=user_row.username,
            full_name=user_row.full_name,
            is_admin=user_row.is_admin,
            created_at=user_row.created_at
        )
    return None


async def pg_upsert_user(*, tg_id: int, username: str) -> User:
    async with pg_session() as session:
        query = (
            insert(users_table)
            .values(tg_id=tg_id, username=username)
            .on_conflict_do_update(index_elements=[users_table.c.tg_id], set_={users_table.c.username: username})
            .returning(users_table)
        )

        result = await session.execute(query)
        user_row = result.fetchone()
        await session.commit()

    assert user_row is not None
    return User(
        id=user_row.id,
        tg_id=user_row.tg_id,
        username=user_row.username,
        full_name=user_row.full_name,
        is_admin=user_row.is_admin,
        created_at=user_row.created_at
    )
