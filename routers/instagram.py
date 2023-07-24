from fastapi import APIRouter
from dependencies import (
    get_images_selenium_inst,
    get_images_selenium_side,
    get_images_bs_side,
)

instagram_router = APIRouter()


@instagram_router.get("/getPhotos/{username}")
async def get_photos_selenium(username: str, max_count: int | None = None):
    imgs = await get_images_selenium_inst(username, max_count)
    return {"urls": imgs}


@instagram_router.get("/getPhotosSide/{username}")
async def get_photos_selenium_side(username: str, max_count: int | None = None):
    imgs = await get_images_selenium_side(username, max_count)
    return {"urls": imgs}


@instagram_router.get("/getPhotosBS/{username}")
async def get_photos_bs_side(username: str, max_count: int | None = None):
    imgs = await get_images_bs_side(username, max_count)
    return {"urls": imgs}
