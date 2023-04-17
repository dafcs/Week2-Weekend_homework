class Room:
    def __init__(self,number):
        self.room_number = number
        self.song_list = []
        self.price = 10
        self.current_guests = []
        self.total_guests = 0

    def count_guests(self):
        return len(self.current_guests)

    def receive_guest(self,guest_list):
        for guest in guest_list:
            self.current_guests.append(guest)

    def can_afford(self,guest_list):
        for guest in guest_list:
            if guest.cash - self.price >= 0:
                guest.cash - self.price
                self.current_guests.append(guest)
            else:
                continue
            
    def add_songs(self,songs):
        for song in songs:
            self.song_list.append(song)

    def check_in_guests(self,guests,songs):
        self.can_afford(guests)
        self.add_songs(songs)

    def count_songs(self):
        return len(self.song_list)