# TODO: Feature 3
from app import app
from src.repositories import movie_repository


def test_search_movies_page():
    test_app = app.test_client()

    response = test_app.get("/movies/search")
    assert b'<p>No Results</p>' in response.data

    response = test_app.get("/movies/search?title=Batman")
    assert b'<p>No Results</p>' in response.data

    movie_repository.create_movie(
        "Inside Out", "Pete Docter", 4)

    response = test_app.get("/movies/search?title=Inside+Out")

    assert b'<td>Result Found:</td>' in response.data
    assert b'<td>Inside Out</td>' in response.data
    assert b'<td>Star rating:</td>' in response.data
    assert b'<td>4</td>' in response.data