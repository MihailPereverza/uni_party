from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class Event:
    id: int
    """ID мероприятия"""
    title: str
    """Название мероприятия"""
    description: str
    """Описание мероприятия"""
    start_time: datetime
    """Время начала"""
    end_time: datetime
    """Время окончания"""
    created_at: datetime
    """Дата создания"""
    created_by: int
    """ID создающего пользователя"""
