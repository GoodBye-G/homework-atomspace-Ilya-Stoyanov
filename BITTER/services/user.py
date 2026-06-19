from database.storage import users, User, posts

SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

def create_user(user_name: str) -> bool:
    """
    Create new user
    
    :param user_name: New user name
    :type user_name: str
    :return: Returns True if the check passes and False if not.
    :rtype: bool
    """
    if any(character in SPECIAL_CHARACTERS for character in user_name):
        return False
    user: User = {
        'name': user_name,
        'followers': [],
        'following': [],
        'posts': []
    }
    users[user_name] = user
    return True

def get_current_user() -> str:
    """
    Log in
    
    :return: Returns the user name
    :rtype: str
    """
    user_name = ""
    while not user_name:
        user_name = input("Your username: ").strip()
    if user_name not in users:
        create_user(user_name)
        print(f"Created a new user: {user_name}")
    else:
        print(f"Welcome back, @{user_name}")
    return user_name


def user_post(creator: str) -> str:
    """
    Provides the user with posts from a specific author at his request
    
    :param creator: the author of the post the user wants to view
    :type creator: str
    :return: A post by a specific author
    :rtype: str
    """
    for post in posts:
        if post.get('author') == creator:
            return (post.get('content'))  
        
def view(id_post: int) -> None:
    """
    shows a post by ID and its number of views
    
    :param id_post: The ID of the post the user wants to view
    :rtn: None
    """
    if id_post < 0 or id_post > len(posts):
        print("Invalid ID")
        return
    post = posts[id_post]
    print(post.get('content'))
    posts[id_post]['views'] += 1
    print(post.get('views'))

def show_user(user_name: str) -> bool :
    """
    Needed to view profiles of a specific user
    
    :param user_name: the name of the user the user wants to view
    :type user_name: str
    :return: To check if a user exists and prevent useless operations and errors
    :rtype: bool
    """

    try:
        user = users[user_name]
        print(f"\n-----{user.get('name')}-----")
        print(f"posts: {user.get('posts')}")
        print(f"followers: {user.get('followers')}")
        print(f"following: {user.get('following')}")
        return True
    except KeyError:
        print("This user does not exist")
        return False
    

def follow(current_user: str, user_name: str) -> None:
    """
    To follow a user
    
    :param current_user
    :type current_user: str
    :param user_name: The user we want to follow
    :type user_name: str
    """


    user = users[user_name]
    (user.get('followers')).append(current_user)

