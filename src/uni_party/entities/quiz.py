from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class Quiz:
    id: int
    """ID квиза"""
    event_id: int
    """ID мероприятия"""
    title: str
    """Название квиза"""
    url: str
    """URL квиза"""
    created_at: datetime
    """Дата создания"""
    created_by: int
    """ID создающего пользователя"""
