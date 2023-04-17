import unittest

from src.guest import *
from src.song import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Mika",25,"There for you","rnb")
        self.guest_2 = Guest("John",30,"Some song","rnb")



    def test_reduce_cash(self):
        self.guest_1.reduce_cash(5)
        self.assertEqual(20,self.guest_1.cash)

