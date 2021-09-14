from movie_model import MovieModel
import requests

def callMovieApi():
    url = '''
    https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20
    '''
    response = requests.get(url)
    
    responseDict = response.json()
    movies = responseDict["data"]["movies"]
    return parsing_model(movies)

def parsing_model(movies):
    movieList = []

    for movie in movies:
        movie_model = MovieModel(movie["title"], movie["rating"], movie["small_cover_image"], movie["summary"] )
        movieList.append(movie_model)
    
    print(movieList)
    return movieList
