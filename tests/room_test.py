import unittest

from src.song import Song
from src.guest import Guest
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Bongo", 3)
        self.room_2 = Room("Studio 24", 5)
    

    def test_room_has_name(self):
        self.assertEqual("Bongo",self.room_1.name)
    

    def test_room_has_capacity(self):
        self.assertEqual(True,isinstance(self.room_1.capacity,int))