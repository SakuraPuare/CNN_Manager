from datetime import datetime

from pydantic import BaseModel


class DetectBase(BaseModel):
    id: int
    user_id: int
    image_id: int
    network_id: int
    output: int
    confidence: float

    created_at: datetime
    updated_at: datetime


class FeedbackBase(BaseModel):
    id: int
    user_id: int
    detect_id: int
    feedback: int

    created_at: datetime
    updated_at: datetime
