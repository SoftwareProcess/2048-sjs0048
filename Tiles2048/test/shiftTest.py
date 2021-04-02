import unittest
import hashlib
import Tiles2048.create as create
import Tiles2048.shift as shift
from pickle import NONE

class ShiftTest(unittest.TestCase):
    
    
    def test_create_ProperGridSize(self):
        userParms = {}
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, "Error: This grid is too small")