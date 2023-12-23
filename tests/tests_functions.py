import unittest
import hash_module
import sys
sys.path.append("..")
from functions import User

class TestCalculatorModule(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_register_valid_username_password(self):
            valid_password = "1234567890"
            user = User("test_user", valid_password)
            self.assertEqual(user.password, valid_password)


    def test_register_invalid_password_length(self):
        with self.assertRaises(ValueError):
            user = User("testUser","1234567891234")
            
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



if __name__ == '__main__':
    unittest.main()
