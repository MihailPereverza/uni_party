import sqlalchemy as sa
from .metadata import metadata

notifications_table = sa.Table(
    'notifications',
    metadata,
    sa.Column('id', sa.BIGINT, autoincrement=True, primary_key=True),
    sa.Column('event_id', sa.BIGINT, sa.ForeignKey('events.id'), nullable=False),
    sa.Column('message', sa.TEXT, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('sent_by', sa.BIGINT, sa.ForeignKey('users.id'), nullable=False),
)
