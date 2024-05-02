import io
import pathlib
from typing import List

import PIL
from fastapi import APIRouter, UploadFile, Depends
from fastapi import Response

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
    images = await ImageSchema.all()
    await LogsSchema.create(user=user, action=f"List image {images}")
    return images


@image_router.post("/")
async def upload_image(file: UploadFile, user: UserSchema = Depends(get_current_user)):
    data = await file.read()
    img = PIL.Image.open(io.BytesIO(data))
    hash = image_hash(img)

    t = await ImageSchema.get_or_none(image_hash=hash)
    if t:
        return t

    types = img.format.lower()
    img.save((upload_folder / hash).with_suffix(f'.{types}'))

    data = await ImageSchema.create(
        user=user,
        name=file.filename,
        image_hash=hash,
        height=img.height,
        width=img.width,
        type=types,
        file_size=len(data)
    )

    await LogsSchema.create(user=user, action=f"Upload image {file.filename}")

    return data


@image_router.get("/{hash}", response_model=ImageBase)
async def detail_image(user: UserSchema = Depends(get_current_user)):
    image_obj = await ImageSchema.get_or_none(image_hash=hash)
    await LogsSchema.create(user=user, action=f"Get image {hash}")
    return image_obj


# return binary image
@image_router.get("/file/{hash}", response_model=bytes)
async def get_image(hash: str, size: float = 1.0):
    image_obj = await ImageSchema.get_or_none(image_hash=hash)
    if not image_obj:
        return {"detail": "Image not found"}

    if size != 1:
        img = PIL.Image.open((upload_folder / hash).with_suffix(f'.{image_obj.type}'))

        # resize image
        img.thumbnail((img.width // size, img.height // size))
        data = io.BytesIO()
        img.save(data, format=image_obj.type)
        data = data.getvalue()
    else:
        data = (upload_folder / hash).with_suffix(f'.{image_obj.type}').read_bytes()

    # response binary image
    return Response(content=data, media_type=f"image/{image_obj.type}")
