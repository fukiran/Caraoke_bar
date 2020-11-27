class Room:
    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guest_list = []
        self.song_list = []


    def add_guest_to_list(self,guest,room):
        if room.capacity == len(room.guest_list):
            return "Room is full, please wait outside"
        if room.entry_fee > guest.cash:
            return "No money, no honey"
        self.guest_list.append(guest)


    def remove_guest_from_list(self,guest,room):
        self.guest_list.remove(guest)


    def add_song_to_list(self,song):
        self.song_list.append(song)
