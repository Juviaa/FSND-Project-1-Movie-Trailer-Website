import webbrowser


class Movie(object):
    '''
    stores information about movies
    '''

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # these are all the attributes for each object of class Movie.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # these are all the methods for each object of class Movie.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)