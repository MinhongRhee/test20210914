
class MovieModel:
    def __init__(self, title, rating, small_cover_image, summary):
        self.title = title
        self.rating = rating
        self.small_cover_image = small_cover_image
        self.summary = summary

class Rating:
    def __init__(self, rating):
        self.rating = rating

class Summary:
    def __init__(self, summary):
        self.summary = summary

class Small_Cover_Image:
    def __init__(self, small_cover_image):
        self.small_cover_image = small_cover_image

class Title:
    def __init__(self, title):
        self.title = title
