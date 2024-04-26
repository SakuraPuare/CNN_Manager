from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.user import UserToken, UserRegister
from router.admin import admin_router
from router.detect import detect_router
from router.image import image_router
from router.network import network_router
from schemas.log import LogsSchema
from schemas.user import UserSchema
from utils import generate_bearer_token

base_router = APIRouter()

base_router.include_router(admin_router)
base_router.include_router(image_router)
base_router.include_router(network_router)
base_router.include_router(detect_router)


@base_router.post("/login", response_model=UserToken)
async def login(user: OAuth2PasswordRequestForm = Depends()):
    user_obj = await UserSchema.get(username=user.username)
    if not user_obj:
        user_obj = await UserSchema.get(email=user.username)
    if not user_obj or user_obj.password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = generate_bearer_token(user_obj)
    user_obj.token = token
    obj = UserToken.model_validate(user_obj)

    await LogsSchema.create(user=user_obj, action=f"User {user_obj.username} logged in")

    return obj


@base_router.post("/register", response_model=UserToken)
async def register(user: UserRegister):
    if (await UserSchema.filter(username=user.username).exists()
            or await UserSchema.filter(email=user.email).exists()):
        raise HTTPException(status_code=400, detail="Username already exists")
    user_obj = await UserSchema.create(**user.dict())
    token = generate_bearer_token(user_obj)
    user_obj.token = token
    obj = UserToken.model_validate(user_obj)

    await LogsSchema.create(user=user_obj, action=f"User {user_obj.username} registered")

    return obj
