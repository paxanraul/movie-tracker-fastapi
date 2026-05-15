from sqlalchemy import select

from models import Movie, User
from schemas import MovieUpdate, MovieCreate


async def get_movies(session):
    result = await session.execute(select(Movie))
    return result.scalars().all()


async def get_movie_id(session, movie_id: int):
    result = await session.execute(select(Movie).where(Movie.id == movie_id))
    return result.scalars().one_or_none()


async def add_movie(session, item: MovieCreate):
    new_movie = Movie(title=item.title, year=item.year)
    session.add(new_movie)
    await session.commit()
    return new_movie


async def delete_movie(session, movie_id: int):
    result = await session.execute(
        select(Movie).where(Movie.id == movie_id)
    )
    movie = result.scalars().one_or_none()

    if movie is None:
        return None

    await session.delete(movie)
    await session.commit()
    return movie

async def update_movie(session, movie_id: int, item: MovieUpdate):
    result = await session.execute(
        select(Movie).where(Movie.id == movie_id)
    )
    movie = result.scalars().one_or_none()

    if movie is None:
        return None

    if item.title is not None:
        movie.title = item.title
    if item.year is not None:
        movie.year = item.year

    await session.commit()
    return movie


async def get_user_by_username(session, username: str):
    result = await session.execute(select(User).where(User.username == username))
    return result.scalars().one_or_none()


async def create_user(session, username: str, password: str):
    user = User(username=username, password=password)
    session.add(user)
    await session.commit()
    return user