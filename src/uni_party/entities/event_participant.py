from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class EventParticipant:
    id: int
    """ID записи"""
    event_id: int
    """ID мероприятия"""
    user_id: int
    """ID пользователя"""
    registered_at: datetime
    """Дата регистрации"""
