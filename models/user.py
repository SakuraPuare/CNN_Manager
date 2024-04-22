from models import Base


class UserBase(Base):
    username: str
    email: str
    is_admin: bool


class UserLogin(Base):
    username: str
    password: str


class UserRegister(Base):
    username: str
    email: str
    password: str


class UserAdminRegister(UserRegister):
    is_admin: bool


class UserToken(UserBase):
    token: str


class UserDetail(UserBase):
    id: int
