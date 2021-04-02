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
        userParms['grid'] = '1024128048163225651264210242566480'
        actualResult = shift._shift(userParms)
        comparison = [1024, 128, 0, 4, 8, 16, 32, 256, 512, 64, 2, 1024, 256, 64, 8, 0]
        self.assertEqual(actualResult, comparison)  