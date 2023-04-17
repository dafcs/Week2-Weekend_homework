import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_list_1 = [
            Guest("Yohy",15,"Bohemian Rapsody","Rock"),
            Guest("Bluey",5,"Bohemian Rapsody","Rock"),
            Guest("Brenn",23,"Brick in the wall","Rock")
        ]

        self.songs = [
            Song("This song"),
            Song("That song")
        ]
        self.room = Room(1)




    def test_receive_and_count_guests(self):
        self.room.receive_guest(self.guest_list_1)
        self.assertEqual(3,self.room.count_guests())

    def test_can_afford(self):
        self.room.can_afford(self.guest_list_1)
        self.assertEqual(2,self.room.count_guests())

    def test_add_songs(self):
        self.room.add_songs(self.songs)
        self.assertEqual(2,self.room.count_songs())

    def test_check_in_guests(self):
        self.room.check_in_guests(self.guest_list_1,self.songs)
        self.assertEqual(2,self.room.count_songs())
        self.assertEqual(2,self.room.count_guests())