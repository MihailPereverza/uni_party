from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, kw_only=True)
class User:
    id: int
    """ID пользователя"""
    tg_id: int
    """ID пользователя в тг"""
    username: str | None
    """Имя пользователя"""
    full_name: str | None
    """Полное имя"""
    is_admin: bool
    """Админ или нет"""
    created_at: datetime
    """Дата создания"""
