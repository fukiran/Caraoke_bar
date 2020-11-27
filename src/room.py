class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guest_list = []
        self.song_list = []


    def add_guest_to_list(self,guest):
        self.guest_list.append(guest)


    def remove_guest_from_list(self,guest):
        self.guest_list.remove(guest)