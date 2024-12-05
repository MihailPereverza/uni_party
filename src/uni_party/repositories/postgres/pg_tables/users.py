import sqlalchemy as sa
from .metadata import metadata

users_table = sa.Table(
    'users',
    metadata,
    sa.Column('id', sa.BIGINT, autoincrement=True, primary_key=True),
    sa.Column('tg_id', sa.BIGINT, nullable=False, unique=True),
    sa.Column('username', sa.VARCHAR(255), nullable=True),
    sa.Column('full_name', sa.VARCHAR(255), nullable=True),
    sa.Column('is_admin', sa.BOOLEAN, nullable=False, default=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False)
)
