import unittest # Importing the unittest module
from app import Account, allacounts # Importing the Account class

class TestAccount(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Instagram","kazungu","1234") # create Account object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account,"Instagram")
        self.assertEqual(self.new_account.username,"kazungu")
        self.assertEqual(self.new_account.password,"1234")

if __name__ == '__main__':
    unittest.main()