from database.storage import users, posts, Post
from typing import Tuple


def create_post(author: str, content: str) -> bool:
    """
    Creating a post
    
    :param author: author of the post
    :type author: str
    :param content: content of the post (the post itself)
    :type content: str
    :return: True if post creation was successful, False if not.
    :rtype: bool
    """
    if author not in users:
        return False
    if not _validate(content):
        return False
    post_id = 1
    if posts:
        post_id = posts[-1]["id"] + 1
    post: Post = {
        "id": post_id,
        "author": author,
        "content": content,
        "likes": [],
        "comments": [],
        "views": 0
    }
    posts.append(post)
    users[author]["posts"].append(post_id)
    return True

banned_words_list = [
    "ads", "abuse", "bet", "bitcoin", "buy", "casino", "cash", "cheap", 
    "claim", "congratulations", "crypto", "dating", "deposit", "dumb", 
    "earnings", "fake", "free", "gamble", "giftcard", "hate", "idiot", 
    "loser", "lottery", "money", "offers", "pills", "poker", "prize", 
    "promo", "sales", "scam", "sexy", "slots", "stupid", "subscribe", 
    "trash", "ugly", "viagra", "win", "winner", "worthless"
]

def _validate(content: str) -> bool:
    """
    Checks the post for criteria: prohibited words, length, etc.
    
    :param content: post that will be validated
    :type content: str
    :return: True if validation is successful, False if not.
    :rtype: bool
    """
    if not content:
        return False
    if len(content) > _MAX_CONTENT_LENGTH:
        return False
    if any(word in content.lower() for word in banned_words_list):
        return False
    return True


_MAX_CONTENT_LENGTH = 280


def rewrite_post(id_post: int, current_user: str) -> None:
    """
    A function for changing or deleting a post at the user's discretion
    
    :param id_post: The ID of the post the user wants to find and edit/delete
    :type id_post: int
    :param current_user: To confirm that the author wants to delete/edit the post
    :type current_user: str
    """
    if id_post < 0 or id_post >= len(posts):
        print("Invalid ID")
        return
    post = posts[id_post]
    if post.get('author') == current_user.strip().lower():
        choice = input("1-Del \n 2-Edit: ").strip()
        if choice == '1':
            posts.pop(id_post)
            print("Deleted")  
        elif choice == '2':
            new_content = input("New text: ").strip()
            if _validate(new_content):
                posts[id_post]['content'] = new_content
                print("Updated")
    else:
        print("You are not the author")

def look_all_post(post) -> Tuple[str, str, int]:
    """
    The function is needed to provide specific post data for further output (author, post, number of views)
    
    :param post: 'Post' is the specific post whose data we are returning.
    :return: Returns the user author, the post itself, and the number of views
    :rtype: Tuple[str, str, int]
    """
    author = post['author']
    post_ = post['content']
    views = post['views']
    return [author, post_, views]
 


   

   
   
   

