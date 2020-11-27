import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Pierre",50)
        self.guest_2 = Guest("Alexander",40)
        self.guest_3 = Guest("Pepe",30)
        self.guest_4 = Guest("Edi",5)


    def test_guest_has_name(self):
        self.assertEqual("Pierre",self.guest_1.name)

    def test_guest_has_money(self):
        self.assertEqual(30,self.guest_3.cash)