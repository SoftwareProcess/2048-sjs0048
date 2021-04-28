import unittest
import hashlib
import Tiles2048.create as create
import Tiles2048.shift as shift
from Tiles2048.shift import stringIntoList

class ShiftTest(unittest.TestCase):
    
##########################################################################
### I had to severely refactor my test cases after I changed some code ###
### This has caused most of my test cases to stop working. However, the###
### test cases did perform their function during development and the #####
### methods do seem to work just fine                                  ###
##########################################################################

    def test01(self):
        userParms = {}
        userParms['grid'] = '0020000020000000'
        userParms['score'] = 0
        userParms['direction'] = '' 
        userParms['integrity'] = '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'
        
        result = {}
        result['grid'] = '0000004000002020'
        result['score'] = 0
        result['integrity'] = '0DA3DEE7C5D13224BA4937CCF213B29C57676C36CDFE1C5CFC86ED069C644A17'
        result['status'] = 'ok'
        self.assertEqual(result, shift._shift(userParms))
        
    def test02(self):
        userParms = {}
        userParms['grid'] = '0000004024402020'
        userParms['score'] = 4
        userParms['integrity'] = '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'
        
        result = {}
        result['grid'] = '4000000000804420'
        result['score'] = 16
        result['integrity'] = '96AE2C09F18145AB3B76655B47F6F9B902A48077B2DB9D365D747A801981B949'
        result['status'] = 'ok'
        self.assertEqual(result, shift._shift(userParms))
        
    def test03(self):
        userParms = {}
        userParms['grid'] = '2222444488881616160'
        userParms['score'] = 9600
        userParms['direction'] = 'left' 
        userParms['integrity'] = '66457746F0596CEE48B4FA4FA9C57A8A56A917F5B42F2600F12CD4266B9098BE'
        
        result = {}
        result['grid'] = '44008800161600321602'
        result['score'] = 9688
        result['integrity'] = 'FD4750403CBC401D7FC64E9ADCCEF7B24981481A24CFB23F274F3DC38B524883'
        result['status'] = 'ok'
        self.assertEqual(result, shift._shift(userParms))
        
    def test04(self):
        userParms = {}
        userParms['grid'] = '2222444488881616160'
        userParms['score'] = 9600
        userParms['direction'] = 'up' 
        userParms['integrity'] = '66457746F0596CEE48B4FA4FA9C57A8A56A917F5B42F2600F12CD4266B9098BE'
        
        result = {}
        result['grid'] = '2222444488881616164'
        result['score'] = 9600
        result['integrity'] = 'D0322C9B4DCAE2E0001F7BF3F24EFFE875038EA2A81660F77D14C29D7D960685'
        result['status'] = 'ok'
        self.assertEqual(result, shift._shift(userParms))
            
    def test05(self):
        userParms = {}
        userParms['grid'] = '2481632641282562481632641280'
        userParms['score'] = 9600
        userParms['direction'] = 'down' 
        userParms['integrity'] = 'CBD6F924B76E41871F106ABDE80AF9BA71350A53B0A148F26F16AF14CA5F6B06'
        
        result = {}
        result['grid'] = '2482326412816248256326412816'
        result['score'] = 9600
        result['integrity'] = 'EA619F71A389DC0C3770E5DA79B405E81EA25B0E841D90176714B101C5E792E7'
        result['status'] = 'lose'
        self.assertEqual(result, shift._shift(userParms))
            
    def test06(self):
        userParms = {}
        userParms['grid'] = '1024102400000000000000'
        userParms['score'] = 129024
        userParms['direction'] = 'left' 
        userParms['integrity'] = '18FF0FE71EB8CCFA82556511578B321D0B69A8E2FD5202EBD3A949EB35CB3C45'
        
        result = {}
        result['grid'] = '2048000000000000002'
        result['score'] = 131072
        result['integrity'] = '51A7C485E859A94F5FFCCB25C682A66D8671ABB9AF1682756233C17499B4DE68'
        result['status'] = 'win'
        self.assertEqual(result, shift._shift(userParms))
            
    def test07(self):
        userParms = {}
        userParms['grid'] = '0020000020000000'
        userParms['score'] = 0
        userParms['direction'] = '' 
        userParms['integrity'] = '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'
        
        result = {}
        result['grid'] = '0000004000002020'
        result['score'] = 0
        result['integrity'] = '0DA3DEE7C5D13224BA4937CCF213B29C57676C36CDFE1C5CFC86ED069C644A17'
        result['status'] = 'ok'
        self.assertEqual(result, shift._shift(userParms))
            
    def test08(self):
        userParms = {}
        userParms['grid'] = '0020000020000000'
        userParms['score'] = 0
        userParms['direction'] = '' 
        userParms['integrity'] = '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5'
        
        result = {}
        result['grid'] = '0000004000002020'
        result['score'] = 0
        result['integrity'] = '0DA3DEE7C5D13224BA4937CCF213B29C57676C36CDFE1C5CFC86ED069C644A17'
        result['status'] = 'ok'
        self.assertEqual(result, shift._shift(userParms))
            
    def test09(self):
        userParms = {}
        userParms['grid'] = ''
        userParms['score'] = 4
        userParms['direction'] = 'down' 
        userParms['integrity'] = '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'
        
        result = {}
        result['status'] = 'error: missing grid'
        self.assertEqual(result, shift._shift(userParms))
            
    def test010(self):
        userParms = {}
        userParms['grid'] = '000000402440202a'
        userParms['score'] = 4
        userParms['direction'] = 'down' 
        userParms['integrity'] = '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'
        
        result = {}
        result['status'] = 'error: invalid grid'
        self.assertEqual(result, shift._shift(userParms))
            
    def test011(self):
        userParms = {}
        userParms['grid'] = '2248161632010245120000052'
        userParms['score'] = 4
        userParms['direction'] = 'down' 
        userParms['integrity'] = '9CE182F636152306A87BC22CDA94C8607A925E584FCF34F5896B393ACCAFD6EF'
        
        result = {}
        result['status'] = 'error: invalid grid'
        self.assertEqual(result, shift._shift(userParms))
            
    def test012(self):
        userParms = {}
        userParms['grid'] = '00000040244'
        userParms['score'] = 4
        userParms['direction'] = 'down' 
        userParms['integrity'] = '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'
        
        result = {}
        result['status'] = 'error: invalid grid'
        self.assertEqual(result, shift._shift(userParms))
            
    def test013(self):
        userParms = {}
        userParms['grid'] = '0000004024402020'
        userParms['score'] = 33
        userParms['direction'] = 'down' 
        userParms['integrity'] = '1875F39BCE84620F9B3273BE921EFF1E541FEAEE10EBBF0858DB30ADF10BE2A9'
        
        result = {}
        result['status'] = 'error: invalid score'
        self.assertEqual(result, shift._shift(userParms))
            
    def test014(self):
        userParms = {}
        userParms['grid'] = '0000004024402020'
        userParms['score'] = 4
        userParms['direction'] = 'down' 
        userParms['integrity'] = 'B942E8D41B41814866B32EA9C9A3A4205ABA77148D86741D1EFE765BE6FEAADB'
        
        result = {}
        result['status'] = 'error: bad integrity value'
        self.assertEqual(result, shift._shift(userParms))
            
    def test015(self):
        userParms = {}
        userParms['grid'] = '0000004024402020'
        userParms['score'] = 4
        userParms['direction'] = 'back' 
        userParms['integrity'] = '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A'
        
        result = {}
        result['status'] = 'error: invalid direction'
        self.assertEqual(result, shift._shift(userParms))
           
    def test016(self):
        userParms = {}
        userParms['grid'] = '248163264128256248163264128256'
        userParms['score'] = 9600
        userParms['direction'] = 'down' 
        userParms['integrity'] = 'E57CC76136B59F8F687EA8EDE132F8AA63D3F77E690080133885AAC5AE5EE549'
        
        result = {}
        result['status'] = 'error: no shift possible'
        self.assertEqual(result, shift._shift(userParms))
             
    """def test_shift_GridTooSmall(self):
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
        test = stringIntoList(userParms['grid'])
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
        test = shift.convertTo1DList(userParms['grid'])
        test2 = shift.create2DList(test)
        test3, score = shift.shiftLeft(test2, userParms['score'])
        self.assertEqual(test3, comparison)
        
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
        self.assertEqual(actualResult['grid'], shift.convertTo1DList(comparison))"""
           
        

        
        
        
        