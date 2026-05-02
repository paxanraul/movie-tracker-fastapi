from contextlib import asynccontextmanager

from sqlalchemy import select
from fastapi import FastAPI
from pydantic import BaseModel

from db import create_db, SessionLocal
from models import Movie


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    yield

app = FastAPI(lifespan=lifespan)
# Classes

class MovieCreate(BaseModel):
    title: str
    year: int


# endpoints
# список всех фильмов
@app.get("/movies")
async def get_movies():
    async with SessionLocal() as session:
        result = await session.execute(select(Movie))
        movies = result.scalars().all()
        return {"movies": movies}


# фильм по индексу, по типу: movies/1 = "Spongebob Squarepants"
@app.get("/movies/{movie_id}")
def get_movie_id(movie_id: int):
    if movie_id >= len(movie_list):
        return {"error": "Movie not found"}
    else:
        return movie_list[movie_id]

# добавить фильм в список
@app.post("/movies")
async def add_movie(item: MovieCreate):
    async with SessionLocal() as session:
        new_movie = Movie(title=item.title, year=item.year)

        session.add(new_movie)
        await session.commit()

        return {"message": "Movie added!"}

# удалить фильм по индексу
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    if movie_id < 0 or movie_id >= len(movie_list):
        return {"error": "Movie not found"}
    else:
        deleted = movie_list.pop(movie_id)
        return {"message": "Movie deleted!", "deleted_movie": deleted, "movies": movie_list}

