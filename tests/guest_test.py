import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Pierre",50,"Gotta Go")
        self.guest_2 = Guest("Alexander",40,"On My Radio")
        self.guest_3 = Guest("Pepe",30,"Divorce a I'ltalienne")
        self.guest_4 = Guest("Edi",5,"Gotta Go")

        self.room_1 = Room("Bongo", 3, 20)
        self.room_2 = Room("Studio 24", 5, 30)

        self.song_1 = Song("Gotta Go", "Agnostic Front", 3.2)
        self.song_2 = Song("On My Radio", "Selecter", 3.52)
        self.song_3 = Song("Divorce a I'ltalienne", "Mungo's Hifi", 3.46)


    def test_guest_has_name(self):
        self.assertEqual("Pierre",self.guest_1.name)


    def test_guest_has_money(self):
        self.assertEqual(30,self.guest_3.cash)


    def test_guest_paying_entry_decreases_cash(self):
        self.guest_1.pay_entry_fee(self.guest_1,self.room_1)
        self.assertEqual(30,self.guest_1.cash)

    def test_if_guest_fav_song_is_in_room(self):
        self.room_1.add_song_to_list(self.song_1)
        self.room_1.add_song_to_list(self.song_2)
        self.assertEqual("Whoo!",self.guest_1.fav_song_in_room(self.guest_1,self.room_1))