from fastapi import APIRouter, HTTPException, Depends

from models.user import UserDetail, UserAdminRegister
from schemas.log import LogsSchema
from schemas.user import UserSchema
from utils import get_current_user

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/list", response_model=list[UserDetail])
async def get_users(page: int = 1, limit: int = 10, user: UserSchema = Depends(get_current_user)):
    users = await UserSchema.all().limit(limit).offset((page - 1) * limit)
    await LogsSchema.create(user=user, action=f"List users {users}")
    return [UserDetail.model_validate(user) for user in users]


@user_router.get("/{user_id}", response_model=UserDetail)
async def get_user(user_id: int, user: UserSchema = Depends(get_current_user)):
    user_obj = await UserSchema.get(id=user_id)
    await LogsSchema.create(user=user, action=f"Get user {user_obj.username}")
    return UserDetail.model_validate(user_obj)


@user_router.post("/create", response_model=UserDetail)
async def create_user(new: UserAdminRegister, user: UserSchema = Depends(get_current_user)):
    # if exist
    if await UserSchema.get_or_none(username=new.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    user_obj = await UserSchema.create(**new.dict())
    await LogsSchema.create(user=user, action=f"Create user {user_obj.username}")
    return UserDetail.model_validate(user_obj)


@user_router.put("/{user_id}", response_model=UserDetail)
async def update_user(user_id: int, new: UserAdminRegister, user: UserSchema = Depends(get_current_user)):
    # if not exist
    old = await UserSchema.get_or_none(id=user_id)
    if not old:
        raise HTTPException(status_code=404, detail="User not found")

    user_obj = await UserSchema.get(id=user_id)

    for key, value in new.dict().items():
        setattr(user_obj, key, value)
    await user_obj.save()

    await LogsSchema.create(user=user, action=f"Update user {user_obj.username}")
    return UserDetail.model_validate(user_obj)


@user_router.delete("/{user_id}")
async def delete_user(user_id: int, user: UserSchema = Depends(get_current_user)):
    user_obj = await UserSchema.get(id=user_id)
    await user_obj.delete()
    await LogsSchema.create(user=user, action=f"Delete user {user_obj.username}")
    return {"message": "User deleted"}
