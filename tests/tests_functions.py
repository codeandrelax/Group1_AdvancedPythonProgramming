import unittest
from unittest.mock import patch
import hash_module
import sys
sys.path.append("..")
from functions import *

class TestCalculatorModule(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        logged_in_users.clear()
        registered_users.clear()

    def test_register_valid_username_password(self,):
            valid_password = "1234567890"
            user = User("test_user", valid_password)
            self.assertEqual(user.password, valid_password)

    
    def test_register_invalid_password_length(self,):
        with self.assertRaises(ValueError):
            user = User("testUser","1234567891234")
        

    @patch("functions.User._validate_password")
    def test_register_invalid_password_length_pass_with_mock(self,mock_validate):
        username="testUser"
        invalid_password="1234567891234"
        mock_validate.return_value=invalid_password
        user = User(username,invalid_password)
        self.assertEqual(user.username,username)
        self.assertEqual(user.password,invalid_password)

    @patch("functions.User.__len__")
    def test_length_of_contact_list(self,mock_len):
        mock_len.return_value=100
        user=User("a","a")
        self.assertEqual(len(user),100)
            
    def test_username_setter(self):
        username="Damjan"
        user=User("Vedran","123")
        user.username=username
        self.assertEqual(user.username,username)

    def test_username_getter(self):
        username="Filip"
        user=User(username,"123")
        self.assertEqual(user.username,username)

    def test_password_setter(self):
        password="321"
        user=User("Vedran","123")
        user.password=password
        self.assertEqual(user.password,password)

    def test_password_getter(self):
        password="321"
        user=User("Vedran",password)
        self.assertEqual(user.password,password)

    def test_login_with_valid_parameters(self):
        username="Vedran Jovanovic"
        password="1234567890"
        register(username, password)
        login(username, password)
        self.assertTrue(username in logged_in_users)

    def test_login_with_invalid_username(self):
        print(registered_users) 
        username="Vedran Jovanovic"
        password="1234567890"
        register(username, password)
        username="Vedran"
        login(username, password)
        self.assertTrue(username not in logged_in_users)
        
    def test_login_with_invalid_password(self):
        print(registered_users) 
        username="Vedran Jovanovic"
        password="1234567890"
        register(username, password)
        password="987654321"
        login(username, password)
        self.assertTrue(username not in logged_in_users)


if __name__ == '__main__':
    unittest.main()
