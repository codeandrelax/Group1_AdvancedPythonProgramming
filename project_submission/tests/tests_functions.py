import unittest
import sys
from unittest.mock import patch
from usrmgm_library import *
from io import StringIO

class TestUserManagement(unittest.TestCase):

    def setUp(self):
        self.hold_output = StringIO()
        sys.stdout = self.hold_output
        # pass

    def tearDown(self):
        sys.stdout = sys.__stdout__
        logged_in_users.clear()
        registered_users.clear()

    def test_register_valid_username_password(self,):
            valid_password = "1234567890"
            user = User("test_user", valid_password)
            self.assertEqual(user.password, valid_password)
  
    def test_register_invalid_password_length(self,):
        with self.assertRaises(ValueError):
            register("testUser","1234567891234")
        
    @patch("usrmgm_library.functions.validate_password")
    def test_register_invalid_password_length_pass_with_mock(self,mock_validate):
        username="testUser"
        invalid_password="1234567891234"
        mock_validate.return_value=invalid_password
        user = User(username,invalid_password)
        self.assertEqual(user.username,username)
        self.assertEqual(user.password,invalid_password)

    @patch("usrmgm_library.User.__len__")
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
        user=User("Vedran","1")
        has_pass=hash_module.hash_password("123")
        user.password="123"
        self.assertEqual(user.password,has_pass)

    def test_password_getter(self):
        password="321"
        user=User("Vedran",password)
        self.assertEqual(user.password,password)

    def test_login_with_valid_params(self):
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
    
    def test_register_with_valid_params(self,):
        username="Filip Adamovic"
        password="1234567890"
        register(username, password)
        self.assertTrue(username in registered_users)

    def test_register_with_invalid_params(self,):
        username="Filip Adamovic"
        password="1234567890987456test"
        with self.assertRaises(ValueError):
            register(username, password)

    @patch("usrmgm_library.hash_module.hash_password")
    @patch("usrmgm_library.functions.validate_password")
    def test_register_with_hash_password_mock(self,mock_hash,mock_validate_password):
        username="Filip Adamovic"
        password="1234567890987456test"
        mock_hash.return_value=password
        mock_validate_password.return_value=password
        created_user=register(username, password)
        self.assertTrue(username in registered_users)
        self.assertEqual(created_user.password,password)

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

    def test_add_contact_valid(self):
        username="James Clerk Maxwell"
        password="5555558"
        user = register(username,password)
        login(username, password)
        add_contact(user, "Isac Newton")
        self.assertEqual(user.contacts, ['Isac Newton'])
        add_contact(user, 'Max Planck')
        self.assertEqual(user.contacts, ['Isac Newton', 'Max Planck'])

    def test_remove_contact_valid(self):
        username="James Clerk Maxwell"
        password="5555558"
        user = register(username,password)
        login(username, password)
        add_contact(user, "Isac Newton")
        add_contact(user, 'Max Planck')
        add_contact(user, 'Erwin Rudolf Josef Alexander Schrodinger')
        self.assertEqual(len(user._contacts), 3)
        remove_contact(user, 'Max Planck')
        self.assertEqual(len(user._contacts), 2)
        remove_contact(user, 'Isac Newton')
        self.assertEqual(len(user._contacts), 1)
        remove_contact(user, 'Erwin Rudolf Josef Alexander Schrodinger')
        self.assertEqual(len(user._contacts), 0)
        e = remove_contact(user, 'Erwin Rudolf Josef Alexander Schrodinger')
        self.assertEqual(e, -1)

    def test_add_contact_with_not_logged_user(self):
        username="James Clerk Maxwell"
        password="5555559"
        user = register(username,password)
        e = add_contact(user, "Isac Newton")
        self.assertEqual(e, -1)

    def test_remove_contact_with_not_logged_user(self):
        username="James Clerk Maxwell"
        password="5555559"
        user = register(username,password)  
        login(username, password)    
        add_contact(user, "Isac Newton")
        add_contact(user, 'Max Planck')
        add_contact(user, 'Erwin Rudolf Josef Alexander Schrodinger')
        self.assertEqual(len(user._contacts), 3)  
        logout(user._username)
        e = remove_contact(user, 'Max Planck')
        self.assertEqual(e, -1)

    def test_print_contact(self):
        username="James Clerk Maxwell"
        password="5555559"
        user = register(username,password)  
        login(username, password)  
        add_contact(user, 'Max Planck')
        add_contact(user, 'Erwin Rudolf Josef Alexander Schrodinger')
        add_contact(user, 'Niels Bohr')
        text = "James Clerk Maxwell's contact list:" + "\n"\
               "Max Planck" + "\n"\
               "Erwin Rudolf Josef Alexander Schrodinger" + "\n"\
               "Niels Bohr" + "\n"\
               "End of James Clerk Maxwell's contact list"
        self.hold_output = StringIO()
        sys.stdout = self.hold_output
        print_contact(user)
        printed_output = self.hold_output.getvalue().strip()
        self.assertEqual(printed_output, text)
        sys.stdout = sys.__stdout__

    def test_print_contact_with_not_logged_uset(self):
        username="James Clerk Maxwell"
        password="5555559"
        user = register(username,password)  
        login(username, password)  
        add_contact(user, 'Max Planck')
        add_contact(user, 'Erwin Rudolf Josef Alexander Schrodinger')
        add_contact(user, 'Niels Bohr')
        logout(user._username)
        text = "User James Clerk Maxwell is not logged in."
        self.hold_output = StringIO()
        sys.stdout = self.hold_output
        print_contact(user)
        printed_output = self.hold_output.getvalue().strip()
        self.assertEqual(printed_output, text)
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
