from flask import Flask, render_template
from utils import movie_selector

app = Flask(__name__)


@app.route('/')
def index():
    current_movies = movie_selector(3)
    return render_template("index.html", movies=current_movies)


if __name__ == "__main__":
    app.run(debug=True)
