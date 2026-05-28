from database.storage import users, User

SPECIAL_SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

def create_user(user_name: str) -> bool:
    if any(character in SPECIAL_SYMBOLS for character in user_name):
        return False
    user: User = {
        'name': user_name,
        'followers': [],
        'folowwing': [],
        'posts': [],
    }
    users[user_name] = user
    return True

def get_current_user() -> str:
    user_name = ""
    while not user_name:
        user_name = input("Your username: ").strip()
    if user_name not in users:
        create_user(user_name)
        print(f"Created a new user: {user_name}")
    else:
        print(f"Welcome back, @{user_name}")
    return user_name
