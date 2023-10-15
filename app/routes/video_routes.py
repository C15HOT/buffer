from fastapi import APIRouter
from pydantic import UUID4

video_router = APIRouter()


@video_router.post("/")
async def save_video_id(video_id: UUID4):
    print(f"сохраняю {video_id}")
