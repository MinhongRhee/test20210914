from movie_model import MovieModel
import requests

url = '''
    https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20
    '''
response = requests.get(url)

responseDict = response.json()
movies = responseDict["data"]["movies"]

movie1 = movies[0]
print(type(movie1["title"]))
print(type(movie1["rating"]))
print(type(movie1["small_cover_image"]))
print(type(movie1["summary"]))