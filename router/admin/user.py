from fastapi import APIRouter, HTTPException, Request

from models.user import UserDetail, UserRegister
from schemas.user import UserSchema

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/{userid}", response_model=UserDetail)
async def get_user(userid: int, request: Request):
    user = request.state.user
    if user.get("id") != userid:
        raise HTTPException(status_code=403, detail="Forbidden")
    user_obj = await UserSchema.get(id=userid)
    return UserDetail.from_orm(user_obj)


@user_router.post("/create", response_model=UserDetail)
async def create_user(user: UserRegister):
    user_obj = await UserSchema.create(**user.dict())
    return UserDetail.from_orm(user_obj)


@user_router.put("/{userid}", response_model=UserDetail)
async def update_user(userid: int, user: UserRegister, request: Request):
    user = request.state.user
    if user.get("id") != userid:
        raise HTTPException(status_code=404, detail="Forbidden")
    user_obj = await UserSchema.get(id=userid)
    await user_obj.update_from_dict(user.dict())
    return UserDetail.from_orm(user_obj)


@user_router.delete("/{userid}")
async def delete_user(userid: int, request: Request):
    user = request.state.user
    if user.get("id") != userid:
        raise HTTPException(status_code=403, detail="Forbidden")
    user_obj = await UserSchema.get(id=userid)
    await user_obj.delete()
    return {"message": "User deleted"}
