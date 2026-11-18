
# TODO: Create your SongCollection class in this file
"""
SongCollection class for CP1404/CP5632 Assignment 2.
"""

import json
from operator import attrgetter

from song import Song


class SongCollection:
    """Represent a collection of Song objects."""

    def __init__(self):
        """Initialise an empty song collection."""
        self.songs = []

    def add_song(self, song):
        """Add a single Song object to the collection."""
        self.songs.append(song)

    def get_number_of_unlearned_songs(self):
        """Return the number of unlearned songs."""
        return sum(1 for song in self.songs if not song.learned)

    def get_number_of_learned_songs(self):
        """Return the number of learned songs."""
        return sum(1 for song in self.songs if song.learned)

    def load_songs(self, filename):
        """Load songs from a JSON file into the collection."""
        try:
            with open(filename, "r", encoding="utf-8") as in_file:
                data = json.load(in_file)
        except FileNotFoundError:
            print(f"ERROR: '{filename}' not found")
            return

        self.songs = []
        for item in data:
            song = Song(
                item["title"],
                item["artist"],
                item["year"],
                item["learned"]
            )
            self.songs.append(song)

    def save_songs(self, filename):
        """Save all songs in the collection to a JSON file."""
        data = []
        for song in self.songs:
            data.append({
                "title": song.title,
                "artist": song.artist,
                "year": song.year,
                "learned": song.learned
            })
        with open(filename, "w", encoding="utf-8") as out_file:
            json.dump(data, out_file, indent=2)

    def sort(self, key):
        """Sort songs by the given key, then by title."""
        self.songs.sort(key=attrgetter(key, "title"))