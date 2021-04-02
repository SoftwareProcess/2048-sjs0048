import unittest
import hashlib
import Tiles2048.create as create
import Tiles2048.shift as shift

class ShiftTest(unittest.TestCase):
    
    
    def test_create_ProperGridSize(self):
        userParms = create._create(None)
        userParms['grid'] = '000020020000000'
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, "Error: This grid is too small.")
        
    def test_create_ProperGridSize2(self):
        userParms = create._create(None)
        userParms['grid'] = '00000000000000000000000000000000000000000000000000000000000000000000000000000000'
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, "Error: This grid is too large.")

    
    def test_create_StringIntoList(self):
        userParms = create._create(None)
        userParms['grid'] = '0000200200000000'
        actualResult = shift._shift(userParms)
        comparison = [0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(actualResult, comparison)  