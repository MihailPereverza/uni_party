import sqlalchemy as sa
from .metadata import metadata

quiz_results_table = sa.Table(
    'quiz_results',
    metadata,
    sa.Column('id', sa.BIGINT, autoincrement=True, primary_key=True),
    sa.Column('quiz_id', sa.BIGINT, sa.ForeignKey('quizzes.id'), nullable=False),
    sa.Column('user_id', sa.BIGINT, sa.ForeignKey('users.id'), nullable=False),
    sa.Column('score', sa.INTEGER, nullable=False),
    sa.Column('completed_at', sa.TIMESTAMP(timezone=True), nullable=False),
)
