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

    def test_contact_getter_setter_deleter(self):
        print(registered_users)
        username="Vedran Jovanovic"
        password="1234567890"
        user = register(username,password)
        login(username, password)
        user.contacts = "Aleksej Avramovic"
        user.contacts = "Albert Einstein"
        add_contact(user, "Isac Newton")
        self.assertEqual(user.contacts, ['Aleksej Avramovic', 'Albert Einstein', 'Isac Newton'])
        del user.contacts[2]
        self.assertEqual(user.contacts, ['Aleksej Avramovic', 'Albert Einstein'])

    def test_len_method(self):
        username="James Clerk Maxwell"
        password="5555557"
        user = register(username,password)
        login(username, password)
        self.assertEqual(len(user), 0)
        user.contacts = "Michael Faraday"
        user.contacts = "Carl Fridrich Gauss"
        user.contacts = "Joseph Henry"
        user.contacts = "Nikola Tesla"
        self.assertEqual(len(user), 4)
        del user.contacts[2]
        self.assertEqual(len(user), 3)

    def test_str_method(self):
        username="James Clerk Maxwell"
        password="5555557"
        user = register(username,password)
        login(username, password)
        user.contacts = "Michael Faraday"
        user.contacts = "Carl Fridrich Gauss"
        self.assertEqual(user.__str__(), 'User: James Clerk Maxwell, Contacts: [\'Michael Faraday\', \'Carl Fridrich Gauss\']')

    def test_iter_method(self):
        username="James Clerk Maxwell"
        password="5555557"
        user = register(username,password)
        login(username, password)
        self.assertEqual(len(user), 0)
        user.contacts = "Michael Faraday"
        user.contacts = "Carl Fridrich Gauss"
        user.contacts = "Joseph Henry"
        user.contacts = "Nikola Tesla"
        c = []
        for contact in user:
            c.append(contact)
        self.assertEqual(c, list(['Michael Faraday', 'Carl Fridrich Gauss', 'Joseph Henry', 'Nikola Tesla']))

    def test_login_with_non_existing_user(self):
        username="James Clerk Maxwell"
        password="5555557"
        e = login(username, password)
        self.assertEqual(e, -1)

    def test_logout(self):
        username="James Clerk Maxwell"
        password="5555558"
        user = register(username,password)
        login(username, password)
        self.assertEqual(user.__str__(), 'User: James Clerk Maxwell, Contacts: []')
        self.assertEqual(len(logged_in_users), 1)
        logout(user._username)
        self.assertEqual(len(logged_in_users), 0)


if __name__ == '__main__':
    unittest.main()
