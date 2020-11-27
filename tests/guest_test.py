import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Pierre")
        self.guest_2 = Guest("Alexander")
        self.guest_3 = Guest("Pepe")


    def test_guest_has_name(self):
        self.assertEqual("Pierre",self.guest_1.name)