from fastapi import APIRouter

import repository
from db import SessionLocal
from schemas import MovieCreate, MovieUpdate

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
)

# список всех фильмов
@router.get("")
async def get_movies():
    async with SessionLocal() as session:
        movies = await repository.get_movies(session)
        return {"movies": movies}

# фильм по индексу, по типу: movies/1 = "Spongebob Squarepants"
@router.get("/{movie_id}")
async def get_movie_id(movie_id: int):
    async with SessionLocal() as session:
        movie = await repository.get_movie_id(session, movie_id)
        if movie is None:
            return {"message": "Movie not found!"}
        return {"movie": movie}

# добавить фильм в список
@router.post("")
async def add_movie(item: MovieCreate):
    async with SessionLocal() as session:
        movie = await repository.add_movie(session, item)
        return {
            "message": "Movie added!",
            "movie": movie,
        }

# удалить фильм по индексу
@router.delete("/{movie_id}")
async def delete_movie(movie_id: int):
    async with SessionLocal() as session:
        movie = await repository.delete_movie(session, movie_id)

        if movie is None:
            return {"message": "Movie not found!"}

        return {"message": "Movie deleted!"}

# обновить данные фильма
@router.patch("/{movie_id}")
async def update_movie(movie_id: int, item: MovieUpdate):
    async with SessionLocal() as session:
        movie = await repository.update_movie(session, movie_id, item)

        if movie is None:
            return {"message": "Movie not found!"}

        return {"message": "Movie updated!", "movie": movie}
