import webbrowser


class Movie(object):
    '''
    Class storing information about movies.

    Args:
        movie_title (str): The title of the movie.
        movie_storyline (str): A one-line summary of the movie.
        poster_image (str): The URL of an image of the movie's poster.
        trailer_youtube (str): The URL of the movie's trailer on YouTube.

    Attributes:
        movie_title (str): The title of the movie.
        movie_storyline (str): A one-line summary of the movie.
        poster_image (str): The URL of an image of the movie's poster.
        trailer_youtube (str): The URL of the movie's trailer on YouTube.

    Methods:
        show_trailer: Plays the trailer for the selected movie.
    '''

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # these are all the methods for each object of class Movie.
    def show_trailer(self):
        '''
        opens the trailer for a particular movie.

        Args:
            None.

        Returns:
            None.
        '''
        webbrowser.open(self.trailer_youtube_url)
