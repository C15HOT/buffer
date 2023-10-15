from fastapi import FastAPI
from uvicorn import run

from app.routes.video_routes import video_router

app = FastAPI(
    title="test",
    description="",
)


app.include_router(video_router)



def main() -> None:
    run(
        app,
        host='0.0.0.0',
        port=8080
    )
