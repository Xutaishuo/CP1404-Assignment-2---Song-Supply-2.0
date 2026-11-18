
# TODO: Create your main program in this file

"""
Name: [XU TAISHUO]
Date started: [11/18/2026]
GitHub URL: [https://github.com/Xutaishuo/CP1404-Assignment-2---Song-Supply-2.0.git]
Kivy GUI program for Song Supply 2.0.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

from song import Song
from songcollection import SongCollection

SONGS_FILE = "songs.json"

LEARNED_COLOUR = (0.4, 0.3, 0.5, 1)
UNLEARNED_COLOUR = (0.1, 0.4, 0.2, 1)


class SongSupplyApp(App):
    """Kivy app for Song Supply 2.0."""

    status_text = StringProperty("")
    sort_options = ("Artist", "Title", "Year")
    sort_key_map = {
        "Artist": "artist",
        "Title": "title",
        "Year": "year",
    }

    def __init__(self, **kwargs):
        """Initialise the app and song collection."""
        super().__init__(**kwargs)
        self.collection = SongCollection()

    def build(self):
        """Build the GUI and load songs."""
        self.title = "Song Supply 2.0"
        self.root = Builder.load_file("app.kv")
        self.collection.load_songs(SONGS_FILE)
        self.update_status(f"Loaded {len(self.collection.songs)} songs from {SONGS_FILE}")
        self.display_songs()
        return self.root

    def on_stop(self):
        """Save songs when the program ends."""
        self.collection.save_songs(SONGS_FILE)

    def display_songs(self):
        """Display song buttons in the right-hand layout."""
        songs_layout = self.root.ids.songs_layout
        songs_layout.clear_widgets()

        sort_option = self.root.ids.sort_spinner.text
        sort_key = self.sort_key_map.get(sort_option, "year")
        self.collection.sort(sort_key)

        for song in self.collection.songs:
            button = Button(
                text=f"{song.title} by {song.artist} ({song.year})",
                size_hint_y=None,
                height=50
            )
            if song.learned:
                button.background_color = LEARNED_COLOUR
                button.text += " (learned)"
            else:
                button.background_color = UNLEARNED_COLOUR
            button.bind(on_release=lambda btn, s=song: self.toggle_song(s))
            songs_layout.add_widget(button)

        self.update_counts()

    def toggle_song(self, song):
        """Toggle a song's learned status and refresh the display."""
        if song.learned:
            song.mark_unlearned()
            self.update_status(f"{song.title} marked as unlearned")
        else:
            song.mark_learned()
            self.update_status(f"{song.title} marked as learned")
        self.display_songs()

    def update_counts(self):
        """Update the top status label with learned and unlearned counts."""
        learned = self.collection.get_number_of_learned_songs()
        unlearned = self.collection.get_number_of_unlearned_songs()
        self.root.ids.count_label.text = f"{unlearned} songs to learn, {learned} songs learned"

    def update_status(self, message):
        """Update the bottom status label."""
        self.status_text = message
        self.root.ids.status_label.text = message

    def sort_songs(self):
        """Refresh display when sorting changes."""
        self.display_songs()

    def add_song(self):
        """Add a new song from the input fields."""
        title = self.root.ids.title_input.text.strip()
        artist = self.root.ids.artist_input.text.strip()
        year_text = self.root.ids.year_input.text.strip()

        if not title or not artist or not year_text:
            self.update_status("Please complete every field")
            return

        try:
            year = int(year_text)
        except ValueError:
            self.update_status("Enter a valid number")
            return

        if year <= 0:
            self.update_status("The year must be > 0")
            return

        song = Song(title, artist, year, False)
        self.collection.add_song(song)
        self.update_status(f"{title} by {artist} ({year}) added")
        self.clear_inputs()
        self.display_songs()

    def clear_inputs(self):
        """Clear input fields and status label."""
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.update_status("")


if __name__ == "__main__":
    SongSupplyApp().run()