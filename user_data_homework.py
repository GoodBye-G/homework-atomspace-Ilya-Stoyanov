UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?/"


def validate_email(user_email:str, mask_email: bool ):

    #check email
    
    if not user_email or not user_email.endswith((".com", ".org", ".ua")) or len(user_email) < 15 or not user_email.count("@") == 1:
        raise  NotImplementedError("Incorrect email")
    
    
    #secret email
        
    if mask_email == True:
        local_email , domain = user_email.split("@")
        secret_email = local_email[1:-1]
        secret_email = user_email.replace(secret_email, len(secret_email) * "*")
        return secret_email
    elif mask_email == False:
        return user_email
    else:
        raise "Inccorect choice"
    



def validate_password(password: str, encrypt_password: bool):
    if not password or not any(letters in UPPERCASE_LETTERS for letters in password) or len(password) < 8 or not any(digits in DIGITS for digits in password):
        raise ValueError("Incorrect password")

    if encrypt_password == True:
        reversed_password = password[::-1]
        return reversed_password
    elif encrypt_password == False:
        return password
    else:
        raise NotImplementedError("Incorrect choice")




def validate_name(full_name: str, show_only_initials: bool):
    surname, name = full_name.split()

    if not full_name or len(full_name.split()) != 2 or len(surname) < 2 or len(name) < 2:
        raise ValueError("Incorrect FULL name")
    
    if show_only_initials == True:
        Initials = f"{surname[0]}.{name[0]}"
        return Initials
    elif show_only_initials == False:
        return full_name
    else:
        raise ValueError
    



def get_user_info():

    user_email = input("enter email: ")
    password = input("enter your password: ")
    full_name = input("enter your full name (surname name): ")
    full_name= full_name.title()
    try:
        mask_email = input("Do you want to disguise your email?(y/n)")
        if mask_email == "y":
            mask_email = True
        elif mask_email == "n":
            mask_email = False
        else:
            raise ValueError("Incorrect email")

        encrypt_password_choice = input("Do you want an encrypted password?(y/n)")
        if encrypt_password_choice == "y":
            encrypt_password = True
        elif encrypt_password_choice == "n":
            encrypt_password = False
        else:
            raise ValueError("Incorrect choice")
        
        user_initials_choice = input("Do you need your initials?(y/n): ")
        if user_initials_choice == "y":
            show_only_initials = True
        elif user_initials_choice == "n":
            show_only_initials = False
        else:
            raise ValueError("Incorrect choice")

        email = validate_email(user_email, mask_email)
        name = validate_name(full_name, show_only_initials)
        user_password = validate_password(password, encrypt_password)
    except ValueError:
        print("Error")

    return(name, user_password, email)




def main():
    print("Hello, this program is for your personal data.")
    try:
        name, user_password, email = get_user_info()
        print(f"\n\n its your name {name}")
        print(f"\n\n Its your password {user_password}")
        print(f"\n\n Its your email {email}")
    except Exception as error:
        print(f"Error:{error}")
    

if __name__ == "__main__":
    main()
