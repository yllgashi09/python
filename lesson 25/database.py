import sqite3

from api import create_user
from models import movie, moviecreate


def create_connection():
    connection = sqlite3.connect('movies.db')
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT NOT NULL
    )
     ''')
    connection,commit()
    connection.close()

create_table()

def create_movie(movie: MovieCreate):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("INSET INTO movies (title, director) VALUES (?,?)", (movie.title,movie.director))
    connection.commit()
    movie_id = cursor.lastrowid
    connection.close()
    return movie_id

def read_movies():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    connection.close()
    movies = [Movie(id=row[0], title=row[1] , direcor=row[2])for row in rows]
    return movies

def read_movie(movie_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
        return Movie(id=row["id"], title=row["title"], director=row["director"])
    def updaate_movie(movie_id: int, movie: MovieCreate) -> bool:
        connection = create_connection()
        cursor = connection.cursor()