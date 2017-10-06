class Movie():
    """Movie

        Attributes:
            title: String. The movie's title.
            poster_image_url: String. The URL for the movie's poster art.
            trailer_youtube_url: String. The URL for the movie's YouTube Trailer
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Inits Movie class with title, poster art and trailer url."""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
