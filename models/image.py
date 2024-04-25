from datetime import datetime

from models import Base


class ImageBase(Base):
    id: int
    user_id: int
    name: str
    description: str | None
    image_hash: str
    height: int
    width: int
    file_size: int
    type: str

    created_at: datetime
    updated_at: datetime
