# TODO: Feature 3
from src.repositories.movie_repository import MovieRepository
from src.models.movie import Movie


def test_get_movie_by_title():
    mymovies = MovieRepository()

    assert None == mymovies.get_movie_by_title("Ice Age")

    mymovies.create_movie("Ice Age", "Chris Wedge", 5)
    result_1 = mymovies.get_movie_by_title("Ice Age")

    assert result_1.title == "Ice Age"
    assert result_1.director == "Chris Wedge"
    assert result_1.rating == 5