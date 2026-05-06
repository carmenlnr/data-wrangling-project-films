import requests
import ast

# 1. Clean Genres (limpieza dataset TMDB de variable género de péliculas). Dataset tiene JSON strings es decir algunas filas están como lista y como string JSON.
def clean_genres(x):
    try:
        if isinstance(x, list):
            return [g["name"] for g in x]
        return [g["name"] for g in ast.literal_eval(x)]
    except:
        return []


# 2. OMDb API
def get_imdb_info(title, api_key):
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    data = requests.get(url).json()

    return {
        "imdb_rating": data.get("imdbRating"),
        "imdb_votes": data.get("imdbVotes"),
        "director": data.get("Director"),
        "year": data.get("Year")
    }

