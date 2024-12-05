import sqlalchemy as sa
from .metadata import metadata

event_participants_table = sa.Table(
    'event_participants',
    metadata,
    sa.Column('id', sa.BIGINT, autoincrement=True, primary_key=True),
    sa.Column('event_id', sa.BIGINT, sa.ForeignKey('events.id'), nullable=False),
    sa.Column('user_id', sa.BIGINT, sa.ForeignKey('users.id'), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(timezone=True), nullable=False),
)
