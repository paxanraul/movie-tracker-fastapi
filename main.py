from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Classes

class Movie(BaseModel):
    name: str


# endpoints
movie_list = ["Whiplash 2013", "Spongebob Squarepants", "Spider-man", "Iron man 3"]

# список всех фильмов
@app.get("/movies")
def get_movies():
    return movie_list


# фильм по индексу, по типу: movies/1 = "Spongebob Squarepants"
@app.get("/movies/{movie_id}")
def get_movie_id(movie_id: int):
    if movie_id >= len(movie_list):
        return {"error": "Movie not found"}
    else:
        return movie_list[movie_id]

# добавить фильм в список
