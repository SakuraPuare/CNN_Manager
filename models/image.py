from models import Base


class ImageBase(Base):
    name: str
    user_id: int
