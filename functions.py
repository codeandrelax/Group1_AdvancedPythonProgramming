
from pydoc import doc
import hash_module
 
import multiprocessing
import time

logged_in_users_lock = multiprocessing.Lock()
logged_in_users = []
registered_users = {}

def logout(username):
    with logged_in_users_lock:
        if username in logged_in_users:
            logged_in_users.remove(username)
            print(f"User {username} is logged out.")
            return 0
        else:
            print(f"User {username} is not logged in.")
            return -1

def login(username, password):
    with logged_in_users_lock:
        if not username in registered_users:
            print("Error: User is not registered. Please try again.")
            return -1
        user = registered_users[username]
        if not hash_module.check_password(user.password, password):
            print("Error: Incorrect password. Please try again.")
            return -1
        if username not in logged_in_users:
            logged_in_users.append(username)
            login_process = multiprocessing.Process(target=login_simulation, args=(username,logged_in_users))
            login_process.start()
            login_process.join()
        else:
            print(f"User {username} is already logged in.")


def login_simulation(username,logged_in_users):
    time.sleep(1)
    print(f"User {username} is logged in.")


def validate_password(password):
    if len(password) > 12 or not password.isdigit():
        raise ValueError("Password must be numeric and have a maximum length of 12")
    return password

def register(username, password):
    if username in registered_users:
        print(f"User '{username}' already exists. Please choose a different username.")
        return None

    hashed_password = hash_module.hash_password(validate_password(password))
    user = User(username, hashed_password)

    registered_users[username] = user   
    print(f"User '{username}' registered successfully.")
    return user

def remove_contact(user,contact_name):
    with logged_in_users_lock:
        if user.username in logged_in_users:
            if contact_name in user.contacts:
                del user.contacts[user.contacts.index(contact_name)]
            else:
                print("There is no requested contact")
                return -1
        else:
            print(f"User {user.username} is not logged in.")
            return -1

def add_contact(user,contact_name):
    with logged_in_users_lock:
        if user.username in logged_in_users:
            if contact_name in user.contacts:
                print("Contact already exists")
            else:
                user.contacts=contact_name    
            return None   
        else:
            print(f"User {user.username} is not logged in.")
            return -1

def print_contact(user):
    with logged_in_users_lock:
        if user.username in logged_in_users:
            print(f"{user.username}'s contact list:")
            for con in user.contacts:
                print(con)
            print(f"End of {user.username}'s contact list") 
            return None    
        else:
            print(f"User {user.username} is not logged in.")

def input_credentials():
    username=input("Enter username: ")
    password=input("Enter password: ")
    return username, password

def select_online_users():
    print("Online users:")
    print("-"*20)

    if len(logged_in_users)==0:
        print("List is empty")
        return
    else:
        for order,user in enumerate(logged_in_users,start=1):
                print(f"{user.ljust(20 - len(str(order)))}{str(order).rjust(len(str(order)))}")
        print("-"*20)
        usr_num=""
        while True:
            try:
                usr_num=int(input("Enter number of user you want to select: "))

                if usr_num < 1 or usr_num >len(logged_in_users):
                    raise ValueError
                else:
                    break

            except (ValueError):
                print("Invalid input! Try again")

        print("-"*20)
        return registered_users[logged_in_users[(usr_num)-1]]

def input_contact_for_user(reg_usr):
    contact=input(f"Enter contact name for {reg_usr}'s contact list: ")
    add_result=add_contact(reg_usr,contact)
    if add_result != -1:
        print("Contact successfully added")

def print_contacts_for_user(reg_usr):
        print_contact(reg_usr)

def remove_contacts_for_user(reg_usr):
        if len(reg_usr.contacts) == 0:
            print("List of contacts is empty")
            return -1
        else:
            print_contact(reg_usr)
            usr_for_del=input("Enter name of contact you want to delete: ")
            del_res=remove_contact(reg_usr,usr_for_del)
            if(del_res != -1):
                print("Contact removed successfully")

def print_online_users():
    print("-"*10,"Online users","-"*10)
    if len(logged_in_users)==0:
        print("There is no online users \n")
        return -1
    else:
        for usr in logged_in_users:
            print(usr)
    print("-"*10,"-"*10)

class User:

    def __init__(self, username, password):
        self._username = username
        self._password = password#self._validate_password(password) - hashed password is already validated
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
        self._password = hash_module.hash_password(self._validate_password(new_password))

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, contact):
        self._contacts.append(contact)

    @contacts.deleter
    def contacts(self, index):
        del self._contacts[index]

    # def __delitem__(self, index):
    #     del self._contacts[index]

    def __len__(self):
        return len(self._contacts)
    
    def __str__(self):
        return f"User: {self._username}, Contacts: {self._contacts}"

    def __iter__(self):
        return iter(self._contacts)

# if __name__ == "__main__":
    # registered_user1 = register("vedran", "1234567890")
    # registered_user2 = register("vedran", "9876543210")

    # print("\nRegistered Users:")
    # for username, user in registered_users.items():
    #     print(f"Username: {username}, Password: {user.password}, Contacts: {user.contacts if user.contacts else 'None'}")

    # login("vedran", "1234567890")
    # print(f"Username: {registered_user1.username}")
    # print(f"Password: {registered_user1.password}")
    # #registered_user1.password = "9876543210" 
    # print(f"New Password: {registered_user1.password}")

    # add_contact(registered_user1,"Aleksej")
    # add_contact(registered_user1,"Filip")
    # add_contact(registered_user1,"Damjan")

    # print(registered_user1)

    # print_contact(registered_user1)
    # print(f"Number of Contacts: {len(registered_user1)}")
  
    # remove_contact(registered_user1,1)
    # print(f"Contacts after deletion:")
    # print_contact(registered_user1)

    # print("\nIterating over contacts:")
    # for contact in registered_user1:
    #     print(contact)



  