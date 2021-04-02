import unittest
import hashlib
import Tiles2048.create as create
import Tiles2048.shift as shift

class ShiftTest(unittest.TestCase):
    
    
    def test_shift_GridTooSmall(self):
        userParms = create._create(None)
        userParms['grid'] = '000020020000000'
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, "Error: This grid is too small. Please check the input string.")

    def test_shift_GridTooLarge(self):
        userParms = create._create(None)
        userParms['grid'] = '10241024102410241024102410241024102410241024102410241024102410240'
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, "Error: This grid is too large. Please check the input string.")
        
    def test_shift_ListInto2dList(self):
        userParms = create._create(None)
        userParms['grid'] = '1024128048163225651264210242566480'
        actualResult = shift._shift(userParms)
        comparison = [[1024, 128, 0, 4], [8, 16, 32, 256], [512, 64, 2, 1024], [256, 64, 8, 0]]
        self.assertEqual(actualResult, comparison)