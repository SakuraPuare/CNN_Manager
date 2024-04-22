from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    is_admin: bool

    class Config:
        orm_mode = True
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str


class UserToken(UserBase):
    token: str


class UserRegister(UserBase):
    password: str


class UserDetail(UserBase):
    id: int
