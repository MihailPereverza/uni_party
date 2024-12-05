import sqlalchemy as sa
from .metadata import metadata

events_table = sa.Table(
    'events',
    metadata,
    sa.Column('id', sa.BIGINT, autoincrement=True, primary_key=True),
    sa.Column('title', sa.VARCHAR(255), nullable=False),
    sa.Column('description', sa.TEXT, nullable=True),
    sa.Column('start_time', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('end_time', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('created_by', sa.BIGINT, sa.ForeignKey('users.id'), nullable=False)
)
