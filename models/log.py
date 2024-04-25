from datetime import datetime

from models import Base


class LogsBase(Base):
    id: int
    user_id: int
    action: str
    created_at: datetime
    updated_at: datetime
