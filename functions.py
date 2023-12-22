
from hash_module import hash_password

registered_users = {}

def register(username, password):
    if username in registered_users:
        print(f"User '{username}' already exists. Please choose a different username.")
        return None

    hashed_password = hash_password(password)
    user = User(username, hashed_password)

    registered_users[username] = user   
    print(f"User '{username}' registered successfully.")
    return user

class User:

    def __init__(self, username, password):
        self._username = username
        self._password = self._validate_password(password)
        self._contacts = []

    def _validate_password(self, password):
        if len(password) > 12:# or not password.isdigit():
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
    registered_user1 = register("vedran", "1234567890")
    registered_user2 = register("vedran", "9876543210")

    print("\nRegistered Users:")
    for username, user in registered_users.items():
        print(f"Username: {username}, Password: {user.password}, Contacts: {user.contacts if user.contacts else 'None'}")

    print(f"Username: {registered_user1.username}")
    print(f"Password: {registered_user1.password}")
    registered_user1.password = "9876543210" 
    print(f"New Password: {registered_user1.password}")

    registered_user1.add_contact("Aleksej")
    registered_user1.add_contact("Filip")
    registered_user1.add_contact("Damjan")

    print(f"Contacts: {registered_user1.contacts}")
    print(f"Number of Contacts: {len(registered_user1)}")

    del registered_user1[1]
    print(f"Contacts after deletion: {registered_user1.contacts}")

    print("\nIterating over contacts:")
    for contact in registered_user1:
        print(contact)