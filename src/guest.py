class Guest:
    def __init__(self,name,cash):
        self.name = name
        self.cash = cash


    def pay_entry_fee(self, guest, room):
        if room.entry_fee < guest.cash:
            guest.cash -= room.entry_fee
         