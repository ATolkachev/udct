import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ['G', 'PG', 'PG-13' 'R']

    def __init__(self, movie_title, movile_storyline, posterImage,
                trailer):
        self.title = movie_title
        self.storyline = movile_storyline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)
