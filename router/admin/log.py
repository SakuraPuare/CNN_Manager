from typing import List

from fastapi import APIRouter, Depends

from models.log import LogsBase
from schemas import LogsSchema, UserSchema
from utils import get_current_user

log_router = APIRouter(prefix="/log", tags=["log"])


@log_router.get("/list", response_model=List[LogsBase])
async def list_logs(page: int = 1, limit: int = 10, user: UserSchema = Depends(get_current_user)):
    logs = await LogsSchema.all().limit(limit).offset((page - 1) * limit)
    await LogsSchema.create(user=user, action=f"List logs {logs}")
    return logs
