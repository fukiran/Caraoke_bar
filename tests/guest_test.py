import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Pierre",50)
        self.guest_2 = Guest("Alexander",40)
        self.guest_3 = Guest("Pepe",30)
        self.guest_4 = Guest("Edi",5)

        self.room_1 = Room("Bongo", 3, 20)
        self.room_2 = Room("Studio 24", 5, 30)


    def test_guest_has_name(self):
        self.assertEqual("Pierre",self.guest_1.name)


    def test_guest_has_money(self):
        self.assertEqual(30,self.guest_3.cash)


    def test_guest_paying_entry_decreases_cash(self):
        self.guest_1.pay_entry_fee(self.guest_1,self.room_1)
        self.assertEqual(30,self.guest_1.cash)