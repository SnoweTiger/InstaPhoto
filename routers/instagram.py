from fastapi import APIRouter
from dependencies import get_images_selenium_side_service, get_images_side_service

instagram_router = APIRouter()


@instagram_router.get("/getPhotosDummy/{username}")
async def get_photos(username: str, max_count: int | None = None):
    print(username, max_count)
    imgs = await get_images_side_service(username, max_count)

    return {"urls": imgs}


@instagram_router.get("/getPhotos/{username}")
async def get_photos(username: str, max_count: int | None = None):
    print(username, max_count)
    imgs = await get_images_selenium_side_service(username, max_count)

    return {"urls": imgs}
