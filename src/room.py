class Room:
    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guest_list = []
        self.song_list = []
        self.till = 100


    def add_guest_to_list(self,guest,room):
        if self.room_is_full(guest, room):
            return "Room is full, please wait outside"
        else:
            if not self.refuse_entry(guest,room):
                guest.pay_entry_fee(guest,room)
                self.guest_list.append(guest)
                self.add_entry_fee_to_till(room)

    def remove_guest_from_list(self,guest,room):
        self.guest_list.remove(guest)


    def add_song_to_list(self,song):
        self.song_list.append(song)

    def check_till(self,room):
        return self.till


    def add_entry_fee_to_till(self,room):
        self.till += self.entry_fee
        

    def refuse_entry(self, guest, room):
        if room.entry_fee > guest.cash:
            return "No money, no caraoke"
        else:
            return False


    def room_is_full(self, guest, room):
        if room.capacity == len(room.guest_list):
            return "Room is full, please wait outside"
        else:
            return False

            
        


        