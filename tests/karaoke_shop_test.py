import unittest

from src.karaoke_shop import KaraokeShop
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestShop(unittest.TestCase):
    def setUp(self):
        #Guest lists
        self.guest_list_1 = [
            Guest("Yohy",10,43,"Bohemian Rapsody","rock"),
            Guest("Bluey",20,37,"Back in Black","rock"),
            Guest("Brenn",15,41,"Brick in the wall","rock")
        ]
        self.guest_list_2 = [
            Guest("Yah",5,17,"Alright","hiphop"),
            Guest("Boh",15,18,"Lose Yourself","hiphop"),
        ]
        self.guest_list_3 = [
            Guest("Aiba",10,23,"Bohemian Rapsody","hiphop"),
            Guest("Lora",20,25,"Lose Yourself","rock"),
            Guest("Gat",30,30,"No favourite","rnb"),
        ]

        self.shop = KaraokeShop("My shop",100)

        self.room_1 = Room(1)
        self.room_2 = Room(2)

        self.guest_1 = Guest("Brenn",23,25,"N#A","Rock")
        self.guest_2 = Guest("Bluey",50,28,"Bohemian Rapsody","rock")
    

    def test_count_active_rooms(self):
        active_rooms = self.shop.count_active_rooms()
        self.assertEqual(0,active_rooms)

    def test_find_free_room(self):
        room_number = self.shop.find_free_room()
        self.assertEqual(1,room_number)

    # def test_find_guest(self):
    #     self.shop.add_to_room(self.guest_1)
    #     # print(self.room_1.room_guests)
    #     # print(self.guest_1.id)
    #     guest = Guest("Bluey",20,37,"Back in Black","rock")
    #     # print(guest.id)
    #     guest_in = self.shop.find_guest_room(guest)
    #     self.assertEqual(1,guest_in)

    def test_add_to_till(self):
        self.shop.add_to_till(self.room_1.fee)
        self.assertEqual(110,self.shop.till)

    def test_suggest_playlist_by_genre(self):
        suggested_playlist = self.shop.suggest_playlist_by_genre(self.guest_list_1)
        compare = self.shop.song_inventory["rock"]
        # print (f'compare list {compare}')
        # print (f'suggested {suggested_playlist}')
        self.assertEqual(compare,suggested_playlist)

    def test_suggest_playlist_by_genre_2(self):
        suggested_playlist = self.shop.suggest_playlist_by_genre(self.guest_list_3)
        compare = self.shop.song_inventory["best of"]
        # print (f'compare list {compare}')
        # print (f'suggested {suggested_playlist}')
        self.assertEqual(compare,suggested_playlist)
        
    def test_check_in(self):
        self.assertEqual(True,self.shop.check_in(self.guest_list_1))

    # def test_play_songs(self):
    #     self.shop.check_in(self.guest_list_1)
    #     liked_songs = self.room_1.play_songs()
    #     self.assertEqual(3,liked_songs)

    # def test_add_room(self):
    #     self.shop.add_room(self.room_1)
    #     self.assertEqual(1,self.shop.count_active_rooms())

    # def test_add_to_empty_room(self):
    #     self.shop.add_to_empty_room(self.guest_list_1)
    #     self.assertEqual(1,self.shop.count_active_rooms())