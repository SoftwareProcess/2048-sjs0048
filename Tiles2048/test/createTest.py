import unittest
import Tiles2048.create as create

class CreateTest(unittest.TestCase):

#  The following is included only for illustrative purposes.  It tests nothing
#  useful.  Please delete and replace with your own test code.

#checks to make sure the size of the string is correct
    def test_create_HappyPathTest010(self):
        userParms = {'op': 'create', 'grid': '16'}
        actualResult = create._create(userParms)
        self.assertIsNotNone(actualResult)
        
        
