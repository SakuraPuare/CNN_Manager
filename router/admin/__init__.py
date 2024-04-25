from fastapi import APIRouter

from router.admin import user, log

admin_router = APIRouter(prefix="/admin", tags=["admin"])

admin_router.include_router(user.user_router)
admin_router.include_router(log.log_router)
