from flask import Flask, render_template
from utils import movie_selector, get_movies

app = Flask(__name__)


@app.route('/')
def index():
    current_movies = movie_selector(1)[0]
    movies = get_movies()
    return render_template("index.html", current=current_movies, movies=movies)


if __name__ == "__main__":
    app.run(debug=True)
