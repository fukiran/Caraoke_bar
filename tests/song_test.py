import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Gotta Go", "Agnostic Front", 3.20)


    def test_song_has_name(self):
        self.assertEqual("Gotta Go", self.song_1.title)
