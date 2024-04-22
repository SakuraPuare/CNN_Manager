from fastapi import APIRouter

from admin import user

admin_router = APIRouter(prefix="/admin", tags=["admin"])

# admin_router.include_router(user.user_router)
