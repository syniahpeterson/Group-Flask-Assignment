# TODO: Feature 2
from src.repositories import movie_repository
from src.models.movie import Movie


def test_create_movie():
    movie = movie_repository.create_movie('Rio', 'Carlos Saldanha', 5)

    assert type(movie) == Movie
    assert movie.title == 'Rio'
    assert movie.director == 'Carlos Saldanha'
    assert movie.rating == 5
    assert movie_repository.get_movie_by_title('Rio') != None