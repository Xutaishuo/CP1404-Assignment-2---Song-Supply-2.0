"""
Tests for the SongCollection class.
"""

from song import Song
from songcollection import SongCollection


def run_tests():
    """Run tests for SongCollection class."""
    # Provided tests (do not change) ...
    # Your additional tests below:

    collection = SongCollection()
    collection.add_song(Song("Heartbreak Hotel", "Elvis Presley", 1956, False))
    collection.add_song(Song("Macarena", "Los Del Rio", 1996, True))
    collection.add_song(Song("Amazing Grace", "John Newton", 1779, True))

    assert len(collection.songs) == 3
    assert collection.get_number_of_unlearned_songs() == 1
    assert collection.get_number_of_learned_songs() == 2

    collection.sort("year")
    assert collection.songs[0].title == "Amazing Grace"
    assert collection.songs[1].title == "Heartbreak Hotel"
    assert collection.songs[2].title == "Macarena"

    print("SongCollection tests passed")


if __name__ == "__main__":
    run_tests()