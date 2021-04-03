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
       
    def test_shift_returnTo1DList(self):
        userParms = create._create(None)
        userParms['grid'] = '1024128048163225651264210242566480'
        actualResult = shift._shift(userParms)
        actualResult2 = shift.convertTo1DList(actualResult)
        comparison = [1024, 128, 0, 4, 8, 16, 32, 256, 512, 64, 2, 1024, 256, 64, 8, 0]
        self.assertEqual(actualResult2, comparison)
        
    def test_shift_listOfIndicesWithZero(self):
        userParms = create._create(None)
        userParms['grid'] = '000200400102400025651232'
        result = shift._shift(userParms)
        resultAs1DList = shift.convertTo1DList(result)
        testResult = shift.indicesOfAllZeros(resultAs1DList)
        comparison = [0, 1, 2, 4, 5, 7, 8, 10, 11, 12]
        self.assertEqual(testResult, comparison)
        
    def test_shift_TransposeOf2DList(self):
        userParms = create._create(None)
        userParms['grid'] = '000200400102400025651232'
        result = shift._shift(userParms)
        testResult = shift.getTranspose(result)
        comparison = [[0, 0, 0, 0], [0, 0, 1024, 256], [0, 4, 0, 512], [0, 256, 512, 32]]
        self.assertEqual(testResult, comparison)
        
    def test_shift_inverseRowsOf2DList(self):
        userParms = create._create(None)
        userParms['grid'] = '000200400102400025651232'
        result = shift._shift(userParms)
        testResult = shift.reverseList(result)
        comparison = [[2, 0, 0, 0], [0, 4, 0, 0], [0, 0, 1024, 0], [32, 512, 256, 0]]
        self.assertEqual(testResult, comparison)