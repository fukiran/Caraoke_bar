import pdb

class Guest:
    def __init__(self, name, cash, fav_song):
        self.name = name
        self.cash = cash
        self.fav_song = fav_song


    def pay_entry_fee(self, guest, room):
        if room.entry_fee < guest.cash:
            guest.cash -= room.entry_fee
    

    def fav_song_in_room(self,guest,room):
        for song in room.song_list:
            if song.title == guest.fav_song:
                return "Whoo!"
           

        