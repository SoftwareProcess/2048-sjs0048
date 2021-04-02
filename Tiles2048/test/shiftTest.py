import unittest
import hashlib
import Tiles2048.create as create
import Tiles2048.shift as shift
from pickle import NONE

class ShiftTest(unittest.TestCase):
    
    
    def test_create_ProperGridSize(self):
        userParms = create._create(None)
        userParms['grid'] = '000020020000000'
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, "Error: This grid is too small")

    
    def test_create_StringIntoList(self):
        userParms = create._create(None)
        userParms['grid'] = '0000200200000000'
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, 0)