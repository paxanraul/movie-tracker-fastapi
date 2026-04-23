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
@app.post("/movies")
def add_movie(item: Movie):
    movie_list.append(item.name)
    return {"message": "Фильм успешно добавлен!", "movies": movie_list}

# удалить фильм по индексу
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    if movie_id >= len(movie_list) or movie_id < 0:
        return {"error": "Movie not found"}
    else:
        deleted = movie_list.pop(movie_id)
        return {"message": "Movie deleted!", "deleted_movie": deleted, "movies": movie_list}

