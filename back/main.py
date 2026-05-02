from contextlib import asynccontextmanager

from sqlalchemy import select, delete
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
async def get_movie_id(movie_id: int):
    async with SessionLocal() as session:
        selected_movie = await session.execute(select(Movie).where(Movie.id == movie_id))
        movie = selected_movie.scalars().one_or_none()
        if movie is None:
            return {"message": "Movie not found!"}
        return {"movie": movie}

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
async def delete_movie(movie_id: int):
    async with SessionLocal() as session:
        selected_movie = await session.execute(delete(Movie).where(Movie.id == movie_id))
        await session.commit()
        return {"message": "Movie deleted!"}


