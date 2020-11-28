import unittest

from src.song import Song
from src.guest import Guest
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Bongo", 3, 20)
        self.room_2 = Room("Studio 24", 5, 30)

        self.guest_1 = Guest("Pierre",50,"Gotta Go")
        self.guest_2 = Guest("Alexander",40,"On My Radio")
        self.guest_3 = Guest("Pepe",30,"Divorce a I'ltalienne")
        self.guest_4 = Guest("Edi",5,"Gotta Go")

        self.song_1 = Song("Gotta Go", "Agnostic Front", 3.2)
        self.song_2 = Song("On My Radio", "Selecter", 3.52)
        self.song_3 = Song("Divorce a I'ltalienne", "Mungo's Hifi", 3.46)


    def test_room_has_name(self):
        self.assertEqual("Bongo",self.room_1.name)
    

    def test_room_has_capacity(self):
        self.assertEqual(True,isinstance(self.room_1.capacity,int))


    def test_room_entry_fee(self):
        self.assertEqual(30, self.room_2.entry_fee)


    def test_guest_list_empty(self):
        self.assertEqual([],self.room_1.guest_list)


    def test_song_list_empty(self):
        self.assertEqual([],self.room_2.song_list)


    def test_add_guest_to_list(self):
        room = self.room_1
        room.add_guest_to_list(self.guest_1,room)
        #check if guest is added to the list
        self.assertEqual(1,len(room.guest_list))
        #check if money is taken from the guest
        self.assertEqual(30,self.guest_1.cash)
        #check if money is added to the till
        self.assertEqual(120,room.check_till(room))
    
    def test_add_guests_to_list(self):
        room = self.room_1
        room.add_guest_to_list(self.guest_1,room)
        room.add_guest_to_list(self.guest_2,room)
        self.assertEqual(2,len(room.guest_list))


    def test_remove_guest_from_list(self):
        room = self.room_1
        room.add_guest_to_list(self.guest_1,room)
        room.remove_guest_from_list(self.guest_1,room)
        self.assertEqual([],room.guest_list)


    def test_song_to_room(self):
        self.room_1.add_song_to_list(self.song_1)
        self.assertEqual(1,len(self.room_1.song_list))


    def test_full_room(self):
        room = self.room_1
        room.add_guest_to_list(self.guest_1,room)
        room.add_guest_to_list(self.guest_2,room)
        room.add_guest_to_list(self.guest_3,room)
        self.assertEqual(room.capacity,len(room.guest_list))
    

    def test_to_many_guests_in_room(self):
        room = self.room_1
        room.add_guest_to_list(self.guest_1,room)
        room.add_guest_to_list(self.guest_2,room)
        room.add_guest_to_list(self.guest_3,room)
        self.assertEqual("Room is full, please wait outside",room.add_guest_to_list(self.guest_4,room))


    def test_to_many_guests_in_room2(self):
        room = self.room_1
        room.add_guest_to_list(self.guest_1,room)
        room.add_guest_to_list(self.guest_2,room)
        room.add_guest_to_list(self.guest_3,room)
        room.add_guest_to_list(self.guest_4,room)
        self.assertEqual(room.capacity,len(room.guest_list))


    def test_check_if_guest_has_enough_money(self):
        self.assertEqual(True,self.room_2.refuse_entry(self.guest_4,self.room_2))


    def test_check_if_guest_has_enough_money2(self):
        self.room_2.add_guest_to_list(self.guest_4,self.room_2)
        self.assertEqual([],self.room_1.guest_list)
    

    def test_check_if_guest_has_enough_money3(self):
        self.room_2.add_guest_to_list(self.guest_3,self.room_2)
        self.assertEqual(1,len(self.room_2.guest_list))


    def test_check_till(self):
        self.assertEqual(self.room_1.till,self.room_1.check_till(self.room_1))


    def test_check_if_fee_add_to_till(self):
        self.room_1.add_entry_fee_to_till(self.room_1)
        self.assertEqual(120,self.room_1.check_till(self.room_1))


    def test_if_guest_fav_song_is_in_room(self):
        self.room_1.add_song_to_list(self.song_1)
        self.assertEqual("Whoo!",self.guest_1.fav_song_in_room(self.guest_1,self.room_1))
    

    # def test_sesion_time_end
    