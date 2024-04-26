from typing import List

from fastapi import APIRouter, Depends

from models.network import NetworkBase, Network
from schemas import LogsSchema, UserSchema
from schemas.network import NetworkSchema
from utils import get_current_user

network_router = APIRouter(prefix="/network", tags=["network"])


@network_router.get("/", response_model=List[Network])
async def get_available_networks(page: int = 1, limit: int = 10, user: UserSchema = Depends(get_current_user)):
    images = await NetworkSchema.all().limit(10).offset((page - 1) * limit)
    await LogsSchema.create(user=user, action=f"List network {images}")
    return images


@network_router.get("/{network_id}", response_model=Network)
async def get_network_detail(network_id: int, user: UserSchema = Depends(get_current_user)):
    network = await NetworkSchema.get_or_none(id=network_id)
    if not network:
        return {"message": "network not found"}

    await LogsSchema.create(user=user, action=f"Get network {network_id}")
    return network


@network_router.post("/")
async def create_network(network: NetworkBase, user: UserSchema = Depends(get_current_user)):
    if await NetworkSchema.get_or_none(name=network.name):
        return {"message": "Network already exists"}

    network_obj = NetworkSchema(**network.dict())
    await network_obj.save()
    await LogsSchema.create(user=user, action=f"Create network {network.name}")
    return {"message": "Network created"}


@network_router.put("/{network_id}")
async def update_network(network_id: int, network: NetworkBase, user: UserSchema = Depends(get_current_user)):
    network_obj = await NetworkSchema.get_or_none(id=network_id)
    if not network_obj:
        return {"message": "Network not found"}

    await network_obj.update_from_dict(network.dict()).save()
    await LogsSchema.create(user=user, action=f"Update network {network_id}")
    return {"message": "Network updated"}


@network_router.delete("/{network_id}")
async def delete_network(network_id: int, user: UserSchema = Depends(get_current_user)):
    network = await NetworkSchema.get_or_none(id=network_id)
    if not network:
        return {"message": "Network not found"}

    await network.delete()
    await LogsSchema.create(user=user, action=f"Delete network {network_id}")
    return {"message": "Network deleted"}
