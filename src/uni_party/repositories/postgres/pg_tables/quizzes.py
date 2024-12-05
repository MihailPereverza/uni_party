import sqlalchemy as sa
from .metadata import metadata

quizzes_table = sa.Table(
    'quizzes',
    metadata,
    sa.Column('id', sa.BIGINT, autoincrement=True, primary_key=True),
    sa.Column('event_id', sa.BIGINT, sa.ForeignKey('events.id'), nullable=False),
    sa.Column('title', sa.VARCHAR(255), nullable=False),
    sa.Column('url', sa.VARCHAR(255), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('created_by', sa.BIGINT, sa.ForeignKey('users.id'), nullable=False),
)
