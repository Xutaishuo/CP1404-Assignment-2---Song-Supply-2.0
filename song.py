"""Song class for CP1404/CP5632 Assignment 2."""


# TODO: Create your Song class in this file
CLASSIC_YEAR = 1975

class Song:
    """Represent a song with title,artist,year and learned status"""
    def __init__(self,title="",artist="",year=0,learned=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.learned = learned
    def __str__(self):
        return f"{self.title}by {self.artist}({self.year})"

    def mark_learned(self):
        """Mark this song as learned."""
        self.learned = True

    def mark_unlearned(self):
        """Mark this song as unlearned."""
        self.learned = False

    def is_classic(self):
        """Return True if the song was released in 1975 or earlier."""
        return self.year <= CLASSIC_YEAR

