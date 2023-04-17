import unittest

from src.guest import *
from src.song import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Mika",27,25,"There for you","rnb")
        self.guest_2 = Guest("Josh",30,33,"Some song","rnb")

    def test_reduce_cash(self):
        self.guest_1.guest_pay(5)
        self.assertEqual(20,self.guest_1.cash)

    def test_reduce_cash_cant_afford(self):
        result = self.guest_1.guest_pay(50)
        self.assertEqual("Can't afford",result)

