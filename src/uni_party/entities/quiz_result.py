from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class QuizResult:
    id: int
    """ID результата"""
    quiz_id: int
    """ID квиза"""
    user_id: int
    """ID пользователя"""
    score: int
    """Результат пользователя"""
    completed_at: datetime
    """Дата завершения"""
