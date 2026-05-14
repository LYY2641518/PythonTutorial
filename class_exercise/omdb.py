import requests

API_KEY = "422fd559"

def search_movie(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url)
