

class User:

    def __init__(self, username, password):
        self._username = username
        self._password = self._validate_password(password)
        self._contacts = []

    def _validate_password(self, password):
        if len(password) > 12 or not password.isdigit():
            raise ValueError("Password must be numeric and have a maximum length of 12")
        return password
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        self._username = new_username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = self._validate_password(new_password)

    @property
    def contacts(self):
        return self._contacts
    
    def add_contact(self, contact):
        self._contacts.append(contact)

    def __delitem__(self, index):
        del self._contacts[index]

    def __len__(self):
        return len(self._contacts)
    
    def __str__(self):
        return f"User: {self._username}, Contacts: {self._contacts}"

    def __iter__(self):
        return iter(self._contacts)
    
if __name__ == "__main__":
    user = User("vedran", "1234567890")

    print(f"Username: {user.username}")
    print(f"Password: {user.password}")
    user.password = "9876543210" 
    print(f"New Password: {user.password}")

    user.add_contact("Aleksej")
    user.add_contact("Filip")
    user.add_contact("Damjan")

    print(f"Contacts: {user.contacts}")
    print(f"Number of Contacts: {len(user)}")

    del user[1]
    print(f"Contacts after deletion: {user.contacts}")

    print("\nIterating over contacts:")
    for contact in user:
        print(contact)