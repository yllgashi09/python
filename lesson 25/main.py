from http.client import  responses

from fastapi import Fastapi, HTTPEception
from typing import List
import database
import modelsfrom modelsimport Movie, MovieCreate

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Welcome to the Movies CRUD API"}

@app.post('/movies/', response_model = Movie)
def create_movie(movie: MovieCreate):
    movie_id= database.create_movie(movie)
    return models.Movie(id=movie_id, **movie.dict())

@app.get("/movies/", response_model= List[Movie])
def read_movies():
    return database.read_movie()

@app.get("/movies/{movie_id}", response_model=Movie)
def read_movie(movie_id: int):
    movie = database.read_movies(movie_id)
    if movie is None:
        raise HTTPException(status_code= 404, detail = "Movie not found")
    return  movie

@app.put("/movies/{movie_id}", response_model= Movie)
def update_movie(movie_id: int, movie: MovieCreate):
    updated = database.update_movie(movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail = "Movie not found")
    return models.Movie(id=movie_id, **movie.dict())

@app.put("/movies/{movie_id}", response_model= dict)
def update_movie(movie_id: int, movie: MovieCreate):
    updated = database.update_movie(movie_id, movie)
    if not deleted:
        raise HTTPException(status_code=404, detail = "Movie not found")
    return models.Movie(id=movie_id, **movie.dict())
