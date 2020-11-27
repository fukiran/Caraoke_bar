import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Gotta Go", "Agnostic Front", 3.2)


    def test_song_has_name(self):
        self.assertEqual("Gotta Go", self.song_1.title)

    def test_song_has_artist_name(self):
        self.assertEqual("Agnostic Front", self.song_1.artist)

    def test_song_has_duration(self):
        self.assertEqual(True,isinstance(self.song_1.duration,float))
