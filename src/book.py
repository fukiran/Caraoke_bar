class Book:
    def __init__(self,name):
        self.name = name
        self.page = {}


    def record_guest_spending(self, guest, room):
            if guest.name in self.page:
                self.page[guest.name] += room.entry_fee
            if guest.name not in self.page:
                self.page[guest.name] = room.entry_fee
