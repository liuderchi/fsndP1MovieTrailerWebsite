"""media.py
Created Date: 20151031

This is a media module contains Movie class.
Movie class contains basic info of a movie.
"""

class Movie():
    """Movie information displayed in web page.

    This class defines all information required for a movie trailer website.

    Attributes:
        title: A string of the movie title.
        storyline: A string of the movie storyline.
        poster_image_url: A string represeting movie poster image URL.
        trailer_youtube_url: A string represeting movie trailer URL.
    """
    def __init__(self, title, storyline, posterImage, youtubeURL):
        """Inits Movie Class."""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = youtubeURL
