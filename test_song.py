from song import Song
import unittest
from datetime import time


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Bout Me", "Wiz Khalifa", "Cabin Fever", "3:30")

    def test_song_str(self):
        self.assertEqual(self.song.__str__(), "Wiz Khalifa - Bout Me from Cabin Fever - 3:30")

    def test_song_set_length(self):
        self.assertEqual(self.song.set_length(), time(0, 3, 30))

    def test_song_length_3(self):
        song3 = Song("Bout Me", "Wiz Khalifa", "Cabin Fever", "1:3:30")
        self.assertEqual(song3.set_length(), time(1, 3, 30))

    def test_song_length_seconds(self):
        self.assertEqual(self.song.length(seconds=True), 3*60 + 30)

    def test_song_length_minutes(self):
        self.assertEqual(self.song.length(minutes=True), 3)

    def test_song_length_hours(self):
        self.assertEqual(self.song.length(hours=True), 0)

    def test_song_length_song(self):
        self.assertEqual(self.song.length(), self.song.set_length().strftime("%h:%M:%S"))

if __name__ == '__main__':
    unittest.main()
