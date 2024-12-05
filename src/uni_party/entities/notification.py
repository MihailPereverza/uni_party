from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class Notification:
    id: int
    """ID уведомления"""
    event_id: int
    """ID мероприятия"""
    message: str
    """Текст уведомления"""
    created_at: datetime
    """Дата создания"""
    sent_by: int
    """ID отправителя"""
