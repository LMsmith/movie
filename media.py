import webbrowser

# define the Movie class
class Movie():

    # Movie has properties for title, storyline, poster image, trailer, release year, actors and summary   
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, year, actors, summary):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year
        self.actors = actors
        self.summary = summary

    # show_trailer function opens the trailer in a modal
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
