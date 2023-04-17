from src.room import Room
from src.song import Song
from src.guest import Guest

class KaraokeShop:
    def __init__(self,name,till):
        self.name = name
        self.till = till
        self.active_rooms = 0
        self.rooms = [
            Room(1),
            Room(2),
            Room(3),
            Room(4),
            Room(5)
        ]
        self.room_count = 0
        self.total_guests_in = 0
        self.song_inventory = {
            "rock":[
            Song("I love Rock 'N Roll","rock"),
            Song("Bohemian Rapsody","rock"),
            Song("Brick in the wall","rock")],
            "rnb":[
            Song("You got it","rnb"),
            Song("Right Now","rnb"),
            Song("There for you","rnb")],
            "hiphop":[
            Song("Alright","hiphop"),
            Song("In da club","hiphop"),
            Song("Lose Yourself","hiphop")],
            "best of":[
            Song("I love Rock 'N Roll","rock"),
            Song("You got it","rnb"),
            Song("Alright","hiphop")
            ]
        }

        self.lobby = []

    # def add_to_empty_room(self,guest_list):
    #     for room in self.rooms:
    #         if room.room_empty():
    #             room.room_guests.extend(guest_list)


    def count_active_rooms(self): #tested
        for room in self.rooms:
            if room.empty_room() == False:
                self.active_rooms +=1
        return self.active_rooms
 
    def find_guest_room(self,guest): #tested
        for room in self.rooms:
            # print(room)
            if room.guest_in_room(guest):
                return room.number
            else:
                print("did not reach")

    def add_to_room(self,room,guest): #tested
            room.add_guest(guest)

    def find_free_room(self): #tested
        for room in self.rooms:
            if room.room_empty():
                return room.number

    def clear_lobby(self):
        self.lobby.clear()

    def add_to_till(self,value): #tested
        self.till += value

    def suggest_playlist_by_genre(self,guest_list): #tested
        wanted_genres = set()
        for guest in guest_list:
            wanted_genres.add(guest.favorite_genre)
        if len(wanted_genres) > 1:
            return self.song_inventory["best of"]
        elif len(wanted_genres) == 1:
            return self.song_inventory[wanted_genres.pop()]

    def check_in(self,guest_list): #tested kind of
        room_number = self.find_free_room()
        if room_number != None:
            self.room = Room(room_number)
            # print(self.room.number)
            if self.room.check_capacity(guest_list):
                # print(self.room.check_capacity(guest_list))
                for guest in guest_list:
                    # print(guest)
                    if guest.can_afford(self.room.fee):
                        # print(guest.can_afford(self.room.fee))
                        guest.guest_pay(self.room.fee)
                        self.add_to_till(self.room.fee)
                        self.room.add_guest(guest)
                        # print(self.room.total_guests)
                    else:
                        self.lobby.append(guest)
                self.room.add_songs(self.suggest_playlist_by_genre(guest_list))
            self.clear_lobby()
            return True
            


    

        

        

            


