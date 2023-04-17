import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.group_1 = [
            Guest("Yohy",150,32,"I love Rock 'N Roll","rock"),
            Guest("Bluey",50,28,"Bohemian Rapsody","rock"),
            Guest("Brenn",23,25,"N#A","rock")
        ]

        self.group_2 = [
            Guest("Donna",375,42,"N#A","N#A")
        ]
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
            "Best of":[
            Song("I love Rock 'N Roll","rock"),
            Song("You got it","rnb"),
            Song("Alright","hiphop")
            ]
        }
        self.room_1 = Room(1)
        self.room_2 = Room(2)
        self.lobby = [self.group_1,self.group_2]

        self.guest_1 = Guest("Brenn",23,25,"N#A","Rock")
        self.guest_2 = Guest("Bluey",50,28,"Bohemian Rapsody","rock")
    
    def test_room_empty(self):
        self.assertEqual(True,self.room_1.room_empty())

    def test_has_capacity(self):
        self.room_1.add_guest(self.guest_1)
        result = self.room_1.has_capacity()
        self.assertEqual(True,result)

    # def test_add_guest_list(self):
    #     self.room_1.add_guest()
    #     self.assertEqual(3,self.room_1.total_guests)
    
    def test_add_songs_to_room(self):
        self.room_1.add_songs(self.song_inventory["rnb"])
        self.assertEqual(3,self.room_1.count_songs())

    # def test_guest_match(self):
    #     guest = Guest("Brenn",23,25,"N#A","Rock")
    #     self.assertEqual(True,guest.guest_match(guest))

    def test_remove_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        # print(self.room_1.total_guests)
        self.room_1.remove_guest(self.guest_1)
        self.assertEqual(1,self.room_1.total_guests)

    def test_guest_in_room(self):
        guest = Guest("Brenn",23,25,"N#A","Rock")
        self.room_1.add_guest(guest)
        self.assertEqual(True,self.room_1.guest_in_room(guest))
    
    # def test_play_songs(self):
    #     self.room_1.add_guest(self.guest_1)
    #     likes = self.room_1.play_songs()
    #     self.assertEqual(1,likes)

