from flask import Flask, render_template, redirect
from utils import movie_selector, get_movies, get_unseen_movies, write_movies

app = Flask(__name__)


@app.route('/')
def index():
    current_movies = movie_selector(1)[0]
    movies = get_movies()
    total_movies = len(movies)
    return render_template("index.html", current=current_movies, movies=movies,
                           total_movies=total_movies,
                           rows=int(total_movies / 4))


@app.route('/watch/<_id>/')
def watch_movie(_id):
    movies = get_movies()
    for movie in movies:
        if movie['id'] == _id:
            movie['is_watch'] = True
            break
    write_movies('movies.json', movies)
    return redirect('/')


@app.route('/unwatch/<_id>/')
def unwatch_movie(_id):
    movies = get_movies()
    for movie in movies:
        if movie['id'] == _id:
            movie['is_watch'] = False
            break
    write_movies('movies.json', movies)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
