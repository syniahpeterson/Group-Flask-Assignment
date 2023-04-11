from flask import Flask, redirect, render_template, request, abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    all_movies = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movies=all_movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    title = request.form.get('title', '')
    director = request.form.get('director', '')
    rating = request.form.get('rating', 0, type=int)
    if title == '' or director == '' or rating == '' or rating < 1 or rating > 5:
        abort(400)
    created_movie = movie_repository.create_movie(title, director, rating)
    return redirect(f'/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    found_movies=[]
    q = request.args.get('q','')
    return render_template('search_movies.html', search_active=True, movies=movie_repository.get_all_movies(), search_query=q)

if __name__ == "__main__":
    app.run(debug=True)