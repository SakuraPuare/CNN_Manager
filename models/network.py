from models import Base


class NetworkBase(Base):
    name: str
    description: str
    network: str
    backend: str
    catalog: str


class Network(NetworkBase):
    id: int
