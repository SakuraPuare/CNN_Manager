from datetime import datetime

from models import Base


class UserLogin(Base):
    username: str
    password: str


class UserRegister(Base):
    username: str
    email: str
    password: str


class UserAdminRegister(UserRegister):
    is_admin: bool


class UserBase(Base):
    username: str
    email: str
    is_admin: bool

    created_at: datetime
    updated_at: datetime


class UserToken(UserBase):
    id: int
    token: str


class UserDetail(UserBase):
    id: int
