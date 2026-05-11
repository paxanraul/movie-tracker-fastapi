from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text

from db import create_db, SessionLocal

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

# проверка на живность
@app.get("/health")
async def health():
    try:
        async with SessionLocal() as session:
            await session.execute(text("SELECT 1"))
        return {"status": "ok", "db": "ok"}
    except Exception:
        raise HTTPException(status_code=503, detail="db unavailable")
