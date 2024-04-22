import io
import pathlib

from PIL import Image
from fastapi import APIRouter, UploadFile, Depends

from schemas.image import ImageSchema
from schemas.user import UserSchema
from utils import image_hash, get_current_user

image_router = APIRouter(prefix="/image", tags=["image"])

upload_folder = pathlib.Path("upload")
upload_folder.mkdir(exist_ok=True)


@image_router.get("/list")
async def list_image(page: int = 1):
    count = await ImageSchema.all().count()
    if count == 0 or page * 10 > count:
        return []

    images = await ImageSchema.all().limit(10).offset((page - 1) * 10)
    return images


@image_router.post("/upload")
async def upload_image(files: list[UploadFile], user: UserSchema = Depends(get_current_user, )):
    success = []
    for file in files:
        data = await file.read()
        img = Image.open(io.BytesIO(data))
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
            file_size=len(data)
        )
        success.append(file.filename)
    if not success:
        return {"message": "No image uploaded", "success": False}
    return {"message": "Upload image success", "success": success}


@image_router.get("/{hash}")
async def detail_image():
    image_obj = await ImageSchema.get_or_none(image_hash=hash)
    return image_obj
