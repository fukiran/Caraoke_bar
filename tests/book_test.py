import unittest

from src.book import Book
from src.guest import Guest
from src.room import Room


class TestBook(unittest.TestCase):
    def setUp(self):

        self.room_1 = Room("Bongo", 3, 20)
        self.room_2 = Room("Studio 24", 5, 30)

        self.guest_1 = Guest("Pierre",50,"Gotta Go")
        self.guest_2 = Guest("Alexander",40,"On My Radio")
        self.guest_3 = Guest("Pepe",30,"Divorce a I'ltalienne")
        self.guest_4 = Guest("Edi",5,"Gotta Go")

        self.book = Book("For taxation purposes")
        self.hiden_book = Book("Real income")


    def test_book_has_name(self):
        self.assertEqual("Real income",self.hiden_book.name)


    def test_if_book_is_empty(self):
        self.assertEqual({},self.book.page)

        
    def test_record_spending_in_book(self):
        self.book.record_guest_spending(self.guest_1,self.room_1)
        self.book.record_guest_spending(self.guest_1,self.room_2)
        self.book.record_guest_spending(self.guest_2,self.room_2)
        self.book.record_guest_spending(self.guest_3,self.room_2)
        self.book.record_guest_spending(self.guest_2,self.room_1)
        self.assertEqual({"Pierre":50,"Alexander":50,"Pepe":30},self.book.page)
        