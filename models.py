from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

    class Config:
        orm_mode = True
        from_attributes = True


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    is_admin: bool
    token: str
