from fastapi import APIRouter, HTTPException

from models import UserLogin, UserToken, UserRegister
from router.admin import admin_router
from schemas import UserSchema
from utils import generate_bearer_token

base_router = APIRouter()

base_router.include_router(admin_router)


@base_router.post("/login", response_model=UserToken)
async def login(user: UserLogin):
    user_obj = await UserSchema.get(username=user.username)
    if not user_obj:
        user_obj = await UserSchema.get(email=user.username)
    if not user_obj or user_obj.password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = generate_bearer_token(user_obj)
    user_obj.token = token
    obj = UserToken.from_orm(user_obj)
    return obj


@base_router.post("/register", response_model=UserToken)
async def register(user: UserRegister):
    if (await UserSchema.filter(username=user.username).exists()
            or await UserSchema.filter(email=user.email).exists()):
        raise HTTPException(status_code=400, detail="Username already exists")
    user_obj = await UserSchema.create(**user.dict())
    token = generate_bearer_token(user_obj)
    user_obj.token = token
    obj = UserToken.from_orm(user_obj)
    return obj
