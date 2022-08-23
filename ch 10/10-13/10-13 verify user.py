import json
def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Promt for a new username"""
    username = input("what is your name?: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        name_check = input(f"are you {username} (yes or no)?: ")
        if name_check == 'yes':
            print(f"welcome back, {username}!")
        elif name_check == 'no':
            get_new_username()
    else:
        greet_new_user()
        
def greet_new_user():
    username = get_new_username()
    print(f"we will remember you when you come back, {username}!")

greet_user()