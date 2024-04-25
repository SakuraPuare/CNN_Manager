import io
import pathlib
from typing import List

import PIL
from fastapi import APIRouter, UploadFile, Depends

from models.image import ImageBase
from schemas.image import ImageSchema
from schemas.log import LogsSchema
from schemas.user import UserSchema
from utils import image_hash, get_current_user

image_router = APIRouter(prefix="/image", tags=["image"])

upload_folder = pathlib.Path("upload")
upload_folder.mkdir(exist_ok=True)


@image_router.get("/list", response_model=List[ImageBase])
async def list_image(page: int = 1, limit: int = 10, user: UserSchema = Depends(get_current_user)):
    images = await ImageSchema.all().limit(10).offset((page - 1) * limit)
    await LogsSchema.create(user=user, action=f"List image {images}")
    return images


@image_router.post("/upload")
async def upload_image(files: List[UploadFile], user: UserSchema = Depends(get_current_user)):
    success = []
    for file in files:
        data = await file.read()
        img = PIL.Image.open(io.BytesIO(data))
        hash = image_hash(img)

        if await ImageSchema.get_or_none(image_hash=hash):
            continue

        types = img.format.lower()
        img.save((upload_folder / hash).with_suffix(f'.{types}'))

        await ImageSchema.create(
            user=user,
            name=file.filename,
            image_hash=hash,
            height=img.height,
            width=img.width,
            type=types,
            file_size=len(data)
        )
        success.append(file.filename)

    await LogsSchema.create(user=user, action=f"Upload image {success}")

    if not success:
        return {"message": "No image uploaded", "success": False}
    return {"message": "Upload image success", "success": success}


@image_router.get("/{hash}", response_model=ImageBase)
async def detail_image(user: UserSchema = Depends(get_current_user)):
    image_obj = await ImageSchema.get_or_none(image_hash=hash)
    await LogsSchema.create(user=user, action=f"Get image {hash}")
    return image_obj
