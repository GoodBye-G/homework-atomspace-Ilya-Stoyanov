from database.storage import users, posts, Post

def create_post(author: str, content: str) -> bool:
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
    if not content:
        return False
    if len(content) > _MAX_CONTENT_LENGTH:
        return False
    if any(word in content.lower() for word in banned_words_list):
        return False
    return True

_MAX_CONTENT_LENGTH = 280
