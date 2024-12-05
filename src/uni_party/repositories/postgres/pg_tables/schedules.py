import sqlalchemy as sa
from .metadata import metadata

schedules_table = sa.Table(
    'schedules',
    metadata,
    sa.Column('id', sa.BIGINT, autoincrement=True, primary_key=True),
    sa.Column('event_id', sa.BIGINT, sa.ForeignKey('events.id'), nullable=False),
    sa.Column('schedule_md', sa.TEXT, nullable=False),
    sa.Column('added_at', sa.TIMESTAMP(timezone=True), nullable=False),
)
