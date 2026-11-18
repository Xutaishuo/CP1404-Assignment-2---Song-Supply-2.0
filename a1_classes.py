"""..."""
# TODO: Copy your first assignment to this file, commit,
# then update to use Song and SongCollection classes


"""
Name: [XU TAISHUO]
Date started: [11/18/2026]
GitHub URL: [https://github.com/Xutaishuo/CP1404-Assignment-2---Song-Supply-2.0.git]
Console program for Song Supply 2.0 using Song and SongCollection classes.
"""
import random
from song import Song
from songcollection import SongCollection

SONGS_FILE = "songs.json"
UNLEARNED_MARKER = "*"
MENU = """D - Display songs
R - Recommend a random song
A - Add a new song
C - Complete a song
Q - Quit"""


def main():
    """Run the console Song Supply program."""
    print("Song Supply 2.0 - by [XU TAISHUO]")

    collection = SongCollection()
    collection.load_songs(SONGS_FILE)
    print(f"{len(collection.songs)} songs loaded")

    while True:
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "D":
            display_songs(collection)
        elif choice == "R":
            recommend_song(collection)
        elif choice == "A":
            add_song(collection)
        elif choice == "C":
            complete_song(collection)
        elif choice == "Q":
            collection.save_songs(SONGS_FILE)
            print(f"{len(collection.songs)} songs saved to {SONGS_FILE}")
            print("Enjoy the music!")
            break
        else:
            print("Invalid menu choice")


def display_songs(collection):
    """Display all songs sorted by year then title."""
    if not collection.songs:
        print("No songs")
        return

    collection.sort("year")
    learned_count = 0

    for number, song in enumerate(collection.songs, 1):
        if song.learned:
            marker = ""
            learned_count += 1
        else:
            marker = f"{UNLEARNED_MARKER}"

        classic_text = " (classic)" if song.is_classic() else ""
        print(f"{number}. {marker}{song.title} - {song.artist} {song.year}{classic_text}")

    unlearned_count = len(collection.songs) - learned_count
    print(f"{learned_count} songs learned, {unlearned_count} songs still to learn")


def recommend_song(collection):
    """Recommend a random unlearned song."""
    unlearned_songs = [song for song in collection.songs if not song.learned]

    if not unlearned_songs:
        print("No songs to learn")
    else:
        song = random.choice(unlearned_songs)
        print(f"Let's learn... {song.title} by {song.artist}")


def add_song(collection):
    """Prompt for a new song and add it to the collection."""
    print("Enter details for a new song.")
    title = get_valid_string("Title: ")
    artist = get_valid_string("Artist: ")
    year = get_valid_integer("Year: ", 1)

    song = Song(title, artist, year, False)
    collection.add_song(song)
    print(f"{title} by {artist} ({year}) added to song list")


def complete_song(collection):
    """Mark an unlearned song as learned."""
    if collection.get_number_of_unlearned_songs() == 0:
        print("No unlearned songs")
        return

    print("Enter the number of a song to mark as learned")
    collection.sort("year")

    while True:
        song_number = get_valid_integer(">>> ", 1, len(collection.songs))
        song = collection.songs[song_number - 1]

        if song.learned:
            print("Song is already learned")
        else:
            song.mark_learned()
            print(f"{song.title} by {song.artist} learned")
            return


def get_valid_string(prompt):
    """Get a non-blank string from the user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input can not be blank")


def get_valid_integer(prompt, minimum, maximum=None):
    """Get an integer within the required range from the user."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Enter a valid integer")
        else:
            if value < minimum:
                print("Number must be > 0")
            elif maximum is not None and value > maximum:
                print("Invalid song number")
            else:
                return value


if __name__ == "__main__":
    main()