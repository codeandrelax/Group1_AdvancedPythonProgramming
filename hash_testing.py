    
import hash_module

def test_hash_password():
    password = "keepyourfriendsclosegetyourenemiestoaster"
    hashed_password = hash_module.hash_password(password)
    print(f"Original Password: {password}")
    print(f"Hashed Password: {hashed_password}")
    return hashed_password

def test_check_password(hashed_password):
    password_to_check = "keepyourfriendsclosegetyourenemiestoaster"
    result = hash_module.check_password(hashed_password, password_to_check)
    if result:
        print("Passwords match!")
    else:
        print("Passwords do not match!")

# Test the hash_password function
hashed_password = test_hash_password()

# Test the check_password function
test_check_password(hashed_password)
