from services.user import get_current_user, user_post, view, show_user, follow
from services.post import create_post, rewrite_post, look_all_post
from database.storage import posts

def show_menu(current_user: str) -> None:
    print("\nWelcome to the bitter, where you can write posts!")
    print(f"You are signed in as: {current_user}")
    print("1. Create post")
    print("2. Look at all posts")
    print("3. Find user's posts")
    print("4. Delete or rewrite post")
    print("5. View post for id")
    print("6. Show user")
    print("7. Exit")



def main() -> None:
    current_user = get_current_user()
    while True:
        show_menu(current_user)
        choice = input('What do you want to do?: ').strip() 

        if choice in ('1', 'create post'):
            content = input("Write your post here: ").strip()
            if create_post(current_user, content):
                print("Your post was created")
            else:
                print("Could not create post. Check the post length.")

        elif choice in ('2', 'look at all posts'):
            for post in posts:
                author, post, views = look_all_post(post)
                print(f"\n----------{author}----------")
                print(f"Author: {author}")
                print(f"Post: {post}")
                print(f"Views: {views}")

        
        elif choice in ('3', 'Find user`s posts'):
            creator = input("enter creator whos post u need check: ")
            print(user_post(creator))
        elif choice in ('4', 'Delete or rewrite'):
            id_post = int(input("Enter the ID of the post you want to delete/rewrite: ")) - 1
            rewrite_post(id_post, current_user)  
        elif choice in ('5', 'Views'):
            id_post = int(input("Enter the ID of the post you want to view: ")) - 1
            view(id_post)
        elif choice in ('6', 'show user'):
            user_name = (input("Enter user`s name: "))
            existing_user = show_user(user_name)
            if existing_user:
                if user_name == current_user:
                    print("You can`t follow yourself")
                else:
                    choice = input("Do you not follow this user?(y/n): ")
                    if choice.lower == "y":
                        follow(current_user, user_name)            
        elif choice in ('7', 'exit'):
            break

main()
