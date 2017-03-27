# Creating a class to store movie info
class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movile_storyline, posterImage, trailer):
        """This is an init function for class movie
        movie_title take title of movie to show on website
        movie_sorytline - takes string of text. This supposed to be storyline
        posterImage - takes string with a link to jpg file. This is a poster image
        trailer - takes a string with a link to youtube to show in modal on a website
        """
        self.title = movie_title
        self.storyline = movile_storyline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailer
