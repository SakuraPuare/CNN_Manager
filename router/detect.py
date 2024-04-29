import pathlib
from typing import List

import torch.cuda
from PIL import Image
from fastapi import APIRouter, Depends

from models.detect import DetectBase, FeedbackBase
from network import *
from router.image import upload_folder
from schemas import UserSchema, ImageSchema, LogsSchema, NetworkSchema, DetectSchema, FeedbackSchema
from utils import get_current_user

detect_router = APIRouter(prefix="/detect", tags=["detect"])

model_path = pathlib.Path("ckpt")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


@detect_router.get("/", response_model=List[DetectBase])
async def get_detection_history(page: int = 1, limit: int = 10, user: UserSchema = Depends(get_current_user)):
    detections = await DetectSchema.all().limit(limit).offset((page - 1) * limit)
    await LogsSchema.create(user=user, action=f"List detections {detections}")
    return detections


@detect_router.post("/")
async def detect(hash: str, model_id: int, user: UserSchema = Depends(get_current_user)):
    file = await ImageSchema.get_or_none(image_hash=hash)
    if not file:
        return {"detail": "Image not found"}

    model = await NetworkSchema.get_or_none(id=model_id)
    if not model.exists():
        return {"detail": "Model not found"}

    net = state.get(model.backend, None)
    if net is None:
        return {"detail": "Model not found"}

    import torch
    import torchvision

    net = net().to(device)
    net.load_state_dict(torch.load(model_path / model.network))
    net.eval()

    file_hash = file.image_hash
    file_suffix = file.type
    file_path = (upload_folder / file_hash).with_suffix(f".{file_suffix}")
    img = Image.open(file_path).convert("RGB")
    img = torchvision.transforms.ToTensor()(img).unsqueeze(0).to(device)
    img = torchvision.transforms.Resize((32, 32))(img)

    output = net(img)
    _, predicted = torch.max(output, 1)

    probability = (torch.nn.functional.softmax(output, dim=1)[0] * 100).tolist()

    ret = {
        "predicted": predicted.item(),
        "probability": probability,
        "labels": eval(model.catalog)
    }

    await DetectSchema.create(user=user, image=file, network=model, output=predicted.item(),
                              confidence=max(probability))
    await LogsSchema.create(user=user, action=f"Detect image {file_hash} with model {model}")
    return ret


@detect_router.get("/feedback", response_model=List[FeedbackBase])
async def get_feedback_history(page: int = 1, limit: int = 10, user: UserSchema = Depends(get_current_user)):
    feedbacks = await FeedbackSchema.all().limit(limit).offset((page - 1) * limit)
    await LogsSchema.create(user=user, action=f"List feedbacks {feedbacks}")
    return feedbacks


@detect_router.get("/feedback/{detect_id}", response_model=FeedbackBase)
async def get_feedback_detail(detect_id: int, user: UserSchema = Depends(get_current_user)):
    feedback = await FeedbackSchema.get_or_none(id=detect_id)
    if not feedback:
        return {"detail": "Feedback not found"}

    await LogsSchema.create(user=user, action=f"Get feedback {detect_id}")
    return feedback


@detect_router.post("/feedback")
async def update(detect_id: int, ground_truth: int, user: UserSchema = Depends(get_current_user)):
    detect = await DetectSchema.get_or_none(id=detect_id)
    if not detect:
        return {"detail": "Detect not found"}

    await FeedbackSchema.create(user=user, detect=detect, feedback=ground_truth)
    await LogsSchema.create(user=user, action=f"Update detect {detect_id} with feedback {ground_truth}")
    return {"detail": "Feedback updated"}


@detect_router.delete("/feedback")
async def delete(detect_id: int, user: UserSchema = Depends(get_current_user)):
    detect = await DetectSchema.get_or_none(id=detect_id)
    if not detect:
        return {"detail": "Detect not found"}

    await detect.delete()
    await LogsSchema.create(user=user, action=f"Delete detect {detect_id}")
    return {"detail": "Detect deleted"}


@detect_router.get("/{detect_id}", response_model=DetectBase)
async def get_detection_detail(detect_id: int, user: UserSchema = Depends(get_current_user)):
    detect = await DetectSchema.get_or_none(id=detect_id)
    if not detect:
        return {"detail": "Detect not found"}

    await LogsSchema.create(user=user, action=f"Get detect {detect_id}")
    return detect
