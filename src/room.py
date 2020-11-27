class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guest_list = []
        self.song_list = []


    def add_guest_to_list(self,guest,room):
        if room.capacity == len(room.guest_list):
            return "Room is full, please wait outside"
        self.guest_list.append(guest)


    def remove_guest_from_list(self,guest,room):
        self.guest_list.remove(guest)


    def add_song_to_list(self,song):
        self.song_list.append(song)