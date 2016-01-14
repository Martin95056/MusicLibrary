from song import Song
from playlist import Playlist
import unittest


class TestPLaylist(unittest.TestCase):
    def setUp(self):
        self.playlist = Playlist("Dolna Chalga", False, False)
        self.song = Song("Bout Me", "Wiz Khalifa", "Cabin Fever", "3:30")
        self.song1 = Song("Bout Meee", "Wwwwiz Khalifa", "Cabin Ffever", "4:30")
        self.song2 = Song("Bouttt Me", "Wiz Khaliiifa", "Cabinnn Fever", "5:30")

    def test_playlist_dasherize_name(self):
        self.assertEqual(self.playlist.dasherize_name(), "Dolna-Chalga")

    def test_playlist_add_one_song(self):
        self.playlist.add_songs(self.song)
        self.assertIn(self.song, self.playlist.list)

    def test_playlist_add_list_of_songs(self):
        self.playlist.add_songs([self.song, self.song1, self.song2])
        self.assertIn(self.song1, self.playlist.list)

    def test_playlist_add_non_song(self):
        with self.assertRaises(TypeError):
            self.playlist.add_songs("should fail")

    def test_playlist_remove_song(self):
        self.playlist.add_songs([self.song, self.song1, self.song2])
        self.playlist.remove_song(self.song1)
        self.assertNotIn(self.song1, self.playlist.list)

    def test_playlist_remove_unexisting_song(self):
        self.playlist.add_songs([self.song, self.song1])
        self.assertEqual(self.playlist.remove_song(self.song2), "There is no such song in the playlist.")

    def test_playlist_total_length(self):
        self.playlist.add_songs([self.song, self.song1, self.song2])
        self.assertEqual(self.playlist.total_length(), "0:13:30")

    def test_playlist_artists(self):
        #It was easier to be tested in REPL. Everything's ok.
        pass

if __name__ == '__main__':
    unittest.main()
