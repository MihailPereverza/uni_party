from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class Schedule:
    id: int
    """ID расписания"""
    event_id: int
    """ID мероприятия"""
    schedule_md: str
    """Расписание в формате Markdown"""
    added_at: datetime
    """Время добавления"""
