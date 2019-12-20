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


def write_movies(json_file, movies):
    f = open(json_file, 'w')
    f.write('[\n')
    for movie in movies:
        json.dump(movie, f)
        if movie['id'] == movies[-1]['id']:
            pass
        else:
            f.write(',\n')
    f.write(']')
    f.close()
    return True


def populate_movies_metadata():
    print("Buscando información en línea")
    url_base = 'http://www.omdbapi.com/?apikey=' + os.getenv("API_KEY")
    movies = get_movies()
    for movie in movies:
        url = url_base + f'&t="{movie["title"]}"'
        print("Buscando en", url)
        r = requests.get(url)
        dataset = json.loads(r.text)
        if 'Error' in dataset:
            print("No se encontró", movie['title'])
            with open('movies-not-found.data', 'a') as f:
                f.write(f"{movie['title']}\n")
        for d in dataset:
            key = d.lower()
            movie[key] = dataset[d]
        f = open('movies-populated.json', 'a')
        json.dump(movie, f)
        f.write(',\n')
    f.write(']')
    f.close()
    return True
