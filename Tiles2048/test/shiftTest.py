import unittest
import hashlib
import Tiles2048.create as create
import Tiles2048.shift as shift
from Tiles2048.shift import stringIntoList

class ShiftTest(unittest.TestCase):
    
    
    def test_shift_GridTooSmall(self):
        userParms = {}
        userParms['grid'] = '000020020000000'
        userParms['direction'] = 'left'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        actualResult = shift._shift(userParms)
        testVal = {}
        testVal['status'] = 'error: invalid grid'
        self.assertEqual(actualResult, testVal)

    def test_shift_GridTooLarge(self):
        userParms = {}
        userParms['grid'] = '10241024102410241024102410241024102410241024102410241024102410240'
        userParms['direction'] = 'left'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        actualResult = shift._shift(userParms)
        testVal = {}
        testVal['status'] = 'error: invalid grid'
        self.assertEqual(actualResult, testVal)
        
    def test_shift_ListInto2dList(self):
        userParms = {}
        userParms['grid'] = '1024128048163225651264210242566480'
        userParms['direction'] = 'left'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        actualResult = shift._shift(userParms)
        comparison = [[1024, 128, 0, 4], [8, 16, 32, 256], [512, 64, 2, 1024], [256, 64, 8, 0]]
        test = stringIntoList(actualResult['grid'])
        self.assertEqual(shift.create2DList(test), comparison)
       
    def test_shift_returnTo1DList(self):
        userParms = {}
        userParms['grid'] = '1024128048163225651264210242566480'
        userParms['direction'] = 'left'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        actualResult = shift._shift(userParms)
        actualResult2 = shift.convertTo1DList(actualResult)
        comparison = [1024, 128, 0, 4, 8, 16, 32, 256, 512, 64, 2, 1024, 256, 64, 8, 0]
        self.assertEqual(actualResult2, comparison)
        
    def test_shift_listOfIndicesWithZero(self):
        userParms = {}
        userParms['grid'] = '000200400102400025651232'
        userParms['direction'] = 'left'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        result = shift._shift(userParms)
        resultAs1DList = shift.convertTo1DList(result)
        testResult = shift.indicesOfAllZeros(resultAs1DList)
        comparison = [0, 1, 2, 4, 5, 7, 8, 10, 11, 12]
        self.assertEqual(testResult, comparison)
        
    def test_shift_TransposeOf2DList(self):
        userParms = {}
        userParms['grid'] = '000200400102400025651232'
        userParms['direction'] = 'left'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        result = shift._shift(userParms)
        testResult = shift.getTranspose(result)
        comparison = [[0, 0, 0, 0], [0, 0, 1024, 256], [0, 4, 0, 512], [2, 0, 0, 32]]
        self.assertEqual(testResult, comparison)
        
    def test_shift_inverseRowsOf2DList(self):
        userParms = {}
        userParms['grid'] = '000200400102400025651232'
        userParms['direction'] = 'left'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        result = shift._shift(userParms)
        testResult = shift.reverseList(result)
        comparison = [[2, 0, 0, 0], [0, 4, 0, 0], [0, 0, 1024, 0], [32, 512, 256, 0]]
        self.assertEqual(testResult, comparison)
        
    def test_shift_SadPathReturnto1DList(self):
        userParms = {}
        userParms['grid'] = '1024128048163225651264210242566480'
        userParms['direction'] = 'left'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        actualResult = shift._shift(userParms)
        
        for i in range(len(actualResult)):     ###this is to remove the last column entirely
            actualResult[i].pop()
    
        actualResult2 = shift.convertTo1DList(actualResult)       
        comparison = [1024, 128, 0, 4, 8, 16, 32, 256, 512, 64, 2, 1024, 256, 64, 8, 0]
        self.assertNotEqual(actualResult2, comparison)
        
    def test_shift_ShiftingLeft(self):
        userParms = {}
        userParms['grid'] = '02022560025600002002'
        userParms['direction'] = 'left'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        actualResult = shift._shift(userParms)
        comparison = [[4, 0, 0, 0], [512, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]
        self.assertEqual(actualResult['grid'], shift.convertTo1DList(comparison))
        
    def test_shift_shiftingRight(self):
        userParms = {}
        userParms['grid'] = '0202000000001024001024'
        userParms['direction'] = 'right'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        actualResult = shift._shift(userParms)
        comparison = [[0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2048]]
        self.assertEqual(actualResult['grid'], shift.convertTo1DList(comparison))
          
    def test_shift_shiftingUp(self):
        userParms = {}
        userParms['grid'] = '4040404000000202'
        userParms['direction'] = 'up'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        actualResult = shift._shift(userParms)
        comparison = [[8, 2, 8, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(actualResult['grid'], shift.convertTo1DList(comparison))
        
    def test_shift_shiftingDown(self):
        userParms = {}
        userParms['grid'] = '2202240004000000'
        userParms['direction'] = 'down'
        userParms['score'] = 4
        encoded = (userParms['grid']  + '.' + str(userParms['score'])).encode()
        integrity = hashlib.sha256(encoded).hexdigest().upper()
        userParms['integrity'] = integrity
        actualResult = shift._shift(userParms)
        comparison = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [4, 8, 0, 2]]
        self.assertEqual(actualResult['grid'], shift.convertTo1DList(comparison))
           
        

        
        
        
        