import unittest
import hashlib
import Tiles2048.create as create
import Tiles2048.shift as shift

class ShiftTest(unittest.TestCase):
    
    
    '''def test_shift_GridTooSmall(self):
        userParms = create._create(None)
        userParms['grid'] = '000020020000000'
        userParms['direction'] = 'left'
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, "Error: This grid is too small. Please check the input string.")

    def test_shift_GridTooLarge(self):
        userParms = create._create(None)
        userParms['grid'] = '10241024102410241024102410241024102410241024102410241024102410240'
        userParms['direction'] = 'left'
        actualResult = shift._shift(userParms)
        self.assertEqual(actualResult, "Error: This grid is too large. Please check the input string.")
        
    def test_shift_ListInto2dList(self):
        userParms = create._create(None)
        userParms['grid'] = '1024128048163225651264210242566480'
        userParms['direction'] = 'left'
        actualResult = shift._shift(userParms)
        comparison = [[1024, 128, 0, 4], [8, 16, 32, 256], [512, 64, 2, 1024], [256, 64, 8, 0]]
        self.assertEqual(actualResult, comparison)
       
    def test_shift_returnTo1DList(self):
        userParms = create._create(None)
        userParms['grid'] = '1024128048163225651264210242566480'
        userParms['direction'] = 'left'
        actualResult = shift._shift(userParms)
        actualResult2 = shift.convertTo1DList(actualResult)
        comparison = [1024, 128, 0, 4, 8, 16, 32, 256, 512, 64, 2, 1024, 256, 64, 8, 0]
        self.assertEqual(actualResult2, comparison)
        
    def test_shift_listOfIndicesWithZero(self):
        userParms = create._create(None)
        userParms['grid'] = '000200400102400025651232'
        userParms['direction'] = 'left'
        result = shift._shift(userParms)
        resultAs1DList = shift.convertTo1DList(result)
        testResult = shift.indicesOfAllZeros(resultAs1DList)
        comparison = [0, 1, 2, 4, 5, 7, 8, 10, 11, 12]
        self.assertEqual(testResult, comparison)
        
    def test_shift_TransposeOf2DList(self):
        userParms = create._create(None)
        userParms['grid'] = '000200400102400025651232'
        userParms['direction'] = 'left'
        result = shift._shift(userParms)
        testResult = shift.getTranspose(result)
        comparison = [[0, 0, 0, 0], [0, 0, 1024, 256], [0, 4, 0, 512], [2, 0, 0, 32]]
        self.assertEqual(testResult, comparison)
        
    def test_shift_inverseRowsOf2DList(self):
        userParms = create._create(None)
        userParms['grid'] = '000200400102400025651232'
        userParms['direction'] = 'left'
        result = shift._shift(userParms)
        testResult = shift.reverseList(result)
        comparison = [[2, 0, 0, 0], [0, 4, 0, 0], [0, 0, 1024, 0], [32, 512, 256, 0]]
        self.assertEqual(testResult, comparison)
        
    def test_shift_SadPathReturnto1DList(self):
        userParms = create._create(None)
        userParms['grid'] = '1024128048163225651264210242566480'
        userParms['direction'] = 'left'
        actualResult = shift._shift(userParms)
        
        for i in range(len(actualResult)):     ###this is to remove the last column entirely
            actualResult[i].pop()
    
        actualResult2 = shift.convertTo1DList(actualResult)       
        comparison = [1024, 128, 0, 4, 8, 16, 32, 256, 512, 64, 2, 1024, 256, 64, 8, 0]
        self.assertNotEqual(actualResult2, comparison)
        
    def test_shift_ShiftingLeft(self):
        userParms = create._create(None)
        userParms['grid'] = '02022560025600002002'
        userParms['direction'] = 'left'
        actualResult = shift._shift(userParms)
        testResult = shift.shiftLeft(actualResult)
        comparison = [[4, 0, 0, 0], [512, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]
        self.assertEqual(testResult, comparison)
        
    def test_shift_shiftingRight(self):
        userParms = create._create(None)
        userParms['grid'] = '0202000000001024001024'
        userParms['direction'] = 'right'
        actualResult = shift._shift(userParms)
        testResult = shift.shiftRight(actualResult)
        comparison = [[0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2048]]
        self.assertEqual(testResult, comparison)
          
    def test_shift_shiftingUp(self):
        userParms = create._create(None)
        userParms['grid'] = '4040404000000202'
        userParms['direction'] = 'up'
        actualResult = shift._shift(userParms)
        testResult = shift.shiftUp(actualResult)
        comparison = [[8, 2, 8, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.assertEqual(testResult, comparison)
        
    def test_shift_shiftingDown(self):
        userParms = create._create(None)
        userParms['grid'] = '2202240004000000'
        userParms['direction'] = 'down'
        actualResult = shift._shift(userParms)
        testResult = shift.shiftDown(actualResult)
        comparison = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [4, 8, 0, 2]]
        self.assertEqual(testResult, comparison)'''
           
        
    def test_shift_Acceptance1(self):
        userParms = create._create(None)
        userParms['grid'] = '2222444488881616160'
        userParms['score'] = 9600
        userParms['direction'] = 'left'
        userParms['integrity'] = '66457746F0596CEE48B4FA4FA9C57A8A56A917F5B42F2600F12CD4266B9098BE'        
        actualResult = shift._shift(userParms)

        comparison = {} 
        comparison['grid'] = '44008800161600321602'
        comparison['score'] = 9688
        comparison['integrity'] = 'FD4750403CBC401D7FC64E9ADCCEF7B24981481A24CFB23F274F3DC38B524883'
        comparison['status'] = 'ok'
        self.assertEqual(actualResult, comparison)
            
            
    def test_shift_Acceptance2(self):
        userParms = create._create(None)
        userParms['grid'] = '2222444488881616160'
        userParms['score'] = 9600
        userParms['direction'] = 'up'
        userParms['integrity'] = '66457746F0596CEE48B4FA4FA9C57A8A56A917F5B42F2600F12CD4266B9098BE'        
        actualResult = shift._shift(userParms)

        comparison = {} 
        comparison['grid'] = '2222444488881616164'
        comparison['score'] = 9600
        comparison['integrity'] = 'D0322C9B4DCAE2E0001F7BF3F24EFFE875038EA2A81660F77D14C29D7D960685'
        comparison['status'] = 'lose'
        self.assertEqual(actualResult, comparison)
            
            
    def test_shift_Acceptance3(self):
        userParms = create._create(None)
        userParms['grid'] = '0000004024402020'
        userParms['score'] = 4
        userParms['direction'] = ''
        userParms['integrity'] = '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'        
        actualResult = shift._shift(userParms)

        comparison = {} 
        comparison['grid'] = '4000000000804420'
        comparison['score'] = 16
        comparison['integrity'] = '96AE2C09F18145AB3B76655B47F6F9B902A48077B2DB9D365D747A801981B949'
        comparison['status'] = 'ok'
        self.assertEqual(actualResult, comparison)
            
        
    def test_shift_Acceptance4(self):
        userParms = create._create(None)
        userParms['grid'] = '1024102400000000000000'
        userParms['score'] = 129024
        userParms['direction'] = 'left'
        userParms['integrity'] = '18FF0FE71EB8CCFA82556511578B321D0B69A8E2FD5202EBD3A949EB35CB3C45'        
        actualResult = shift._shift(userParms)

        comparison = {} 
        comparison['grid'] = '2048000000000000002'
        comparison['score'] = 131072
        comparison['integrity'] = '51A7C485E859A94F5FFCCB25C682A66D8671ABB9AF1682756233C17499B4DE68'
        comparison['status'] = 'win'
        self.assertEqual(actualResult, comparison)
                
        
        
        
        
        
        
        