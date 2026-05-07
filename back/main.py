from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from db import create_db

from router import router as movies_router

BASE_DIR = Path(__file__).resolve().parent.parent
FRONT_DIR = BASE_DIR / "front"


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory=FRONT_DIR), name="static")
app.include_router(movies_router)



# подключение к frontend
@app.get("/")
async def frontend():
    return FileResponse(FRONT_DIR / "index.html")
