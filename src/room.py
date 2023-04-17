class Room():
    def __init__(self,number):
        self.number = number
        self.song_list = []
        self.fee = 10
        self.capacity = 5
        self.room_guests = []
        self.total_guests = 0


    def room_empty(self): #tested
        return self.total_guests == 0

    def has_capacity(self): #tested
        return self.total_guests < 6
    
    def add_guest(self,guest): #tested
            if self.total_guests + 1 > self.capacity:
                return "Room Full"
            else:
                self.room_guests.append(guest)
                self.total_guests += 1     
            #guest represents a song object, which is an individual instance and not iterable
            #.append needs to be used
    
    def add_songs(self, playlist): #tested
        self.song_list.extend(playlist) 
            #extend appends the elements of an iterable object, in this case the list value
            #Could add a for loop but this is less verbose

    def remove_guest(self,guest_to_remove):
        for guest in range(len(self.room_guests)-1,-1,-1):
            if self.room_guests[guest].id == guest_to_remove.id:
                del self.room_guests[guest]
        self.total_guests -= 1

    def empty_room(self):
        self.room_guests.clear()

    def count_songs(self): #tested
        counter = 0
        for song in self.song_list:
            counter += 1
        return counter

    def guest_in_room(self,guest):
        for guests in self.room_guests:
            if guests.id == guest.id:
                return True
            else:
                return False
            
    def count_guests(self):
        self.total_guests = len(self.current_guests)

    def check_capacity(self,guest_list):
        return len(guest_list) <= self.capacity

    # def check_song(self):
    #     for song in self.song_list:
    #         song.equals()

    def play_songs(self):
        room_song = ""
        likes = 0
        for song in self.song_list:
            room_song = song
            for guest in self.room_guests:
                if guest.favorite_song == room_song.name:
                    likes += 1
        return likes
                    
        






    # def remove_guest(self,guest_to_remove):
    #     print("Guest to remove:", id(guest_to_remove))
    #     print("Guests in room:", [id(guest) for guest in self.room_guests])
    #     for guest in range(len(self.room_guests)-1, -1, -1):
    #         if self.room_guests[guest] == guest_to_remove:
    #             del self.room_guests[guest]
    #             self.total_guests -= 1
    #     print("Guests after removal:", [id(guest) for guest in self.room_guests])

    
    # def remove_guest(self,guest_to_remove):
    #         for guest in range(len(self.room_guests)-1, -1, -1):
    #             # print(guest)
    #             if self.room_guests[guest].guest_match(guest_to_remove):
    #                 del self.room_guests[guest]
    #                 self.total_guests -= 1
            #range(start,stop,[step])
            #range takes the starting index, end index and the optional step
            #start default is 0
            #we are stopping at -1 because we want to iterate 0 last
            #step is optional, in this case we are asking it to index - 1
    
