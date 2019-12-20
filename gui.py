from flask import Flask, render_template, redirect
from utils import (movie_selector, get_movies, get_unseen_movies,
                   write_movies, get_current_movies)

app = Flask(__name__)


@app.route('/')
def index():
    current_movies = get_current_movies()
    movies = get_movies()
    total_movies = len(movies)
    if not current_movies:
        current_movies = movie_selector(1)[0]
        for movie in movies:
            if movie['id'] == current_movies['id']:
                movie['is_current'] = True
                break
        write_movies('movies.json', movies)
    else:
        current_movies = current_movies[0]
    return render_template("index.html", current=current_movies, movies=movies,
                           total_movies=total_movies,
                           rows=int(total_movies / 4))


@app.route('/watch/<_id>/')
def watch_movie(_id):
    movies = get_movies()
    for movie in movies:
        if movie['id'] == _id:
            movie['is_watch'] = True
            movie['is_current'] = False
            break
    write_movies('movies.json', movies)
    return redirect('/')


@app.route('/unwatch/<_id>/')
def unwatch_movie(_id):
    movies = get_movies()
    for movie in movies:
        if movie['id'] == _id:
            movie['is_watch'] = False
            movie['is_current'] = False
            break
    write_movies('movies.json', movies)
    return redirect('/')


@app.route('/fav/<_id>/')
def set_fav(_id):
    movies = get_movies()
    for movie in movies:
        if movie['id'] == _id:
            movie['is_fav'] = True
            break
    write_movies('movies.json', movies)
    return redirect('/')


@app.route('/unfav/<_id>/')
def unset_fav(_id):
    movies = get_movies()
    for movie in movies:
        if movie['id'] == _id:
            movie['is_fav'] = False
            break
    write_movies('movies.json', movies)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
