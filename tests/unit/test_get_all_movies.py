# TODO: Feature 1
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie


def test_get_all_movies_method():
    movies = [Movie("Up", "Pete Docter", 3), Movie("Inside Out", "Pete Docter", 4), Movie("Rio", "Carlos Saldanha", 5)]
    movie_repository_singleton.create_movie("Up", "Pete Docter", 3)
    movie_repository_singleton.create_movie("Inside Out", "Pete Doctor", 4)
    movie_repository_singleton.create_movie("Rio", "Carlos Saldanha", 5)
    singleton_movies = movie_repository_singleton.get_all_movies()
    for movie in range(3):
        assert type(singleton_movies[movie]) is Movie
        assert singleton_movies[movie].title == movies[movie].title
        assert singleton_movies[movie].director == movies[movie].director
        assert singleton_movies[movie].rating == movies[movie].rating