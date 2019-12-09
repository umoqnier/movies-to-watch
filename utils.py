import os
import random
import json
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


def movie_selector(movies_to_watch=1):
    movies = get_unseen_movies()
    movies_to_watch = random.choices(movies, k=movies_to_watch)
    return movies_to_watch


def get_unseen_movies():
    with open('movies.json', 'r') as f:
        raw_movies = f.read()
    movies = json.loads(raw_movies)
    return [m for m in movies if not m['is_watch']]


def get_movies():
    with open('movies.json', 'r') as f:
        raw_movies = f.read()
    movies = json.loads(raw_movies)
    return movies


def populate_movies_metadata():
    url_base = 'http://www.omdbapi.com/?apikey=' + os.getenv("API_KEY")
    movies = get_movies()
    breakpoint()
    for movie in movies:
        url = url_base + f'&t="{movie["name"]}"'
        r = requests.get(url)
    # TODO: Manejar información del API
    return []


populate_movies_metadata()

