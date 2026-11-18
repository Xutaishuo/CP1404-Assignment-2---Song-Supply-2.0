"""
Tests for the Song class.
"""

from song import Song


def run_tests():
    """Run tests for Song class."""
    # Provided tests (do not change) ...
    # Your additional tests below:

    song = Song("Heartbreak Hotel", "Elvis Presley", 1956, False)

    # Test __str__
    assert str(song) == "Heartbreak Hotel by Elvis Presley (1956)"

    # Test is_classic
    assert song.is_classic() is True
    classic_song = Song("Amazing Grace", "John Newton", 1779, True)
    assert classic_song.is_classic() is True
    modern_song = Song("Macarena", "Los Del Rio", 1996, True)
    assert modern_song.is_classic() is False

    # Test mark_learned and mark_unlearned
    song.mark_learned()
    assert song.learned is True
    song.mark_unlearned()
    assert song.learned is False

    print("Song tests passed")


if __name__ == "__main__":
    run_tests()