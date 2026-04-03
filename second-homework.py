# #Завдання 1 -Iнiцiали

full_name = input("Введiть своє iм`я ты прiзвище(Name Surname)")

name , surname = full_name.split() 
print (f"Iнiцiали: {name[0]}, {surname[0]}")



# #Завдання 2 -Маскування email
mail = input("Введiть свою електрону пошту: ")

if not mail or not mail.endswith((".com" , ".org")):
    print ("Неправильно написана пошта")
else:
    pass


mail_name , domain = mail.split("@")

secret_mail = mail_name[1:-1]
secret_mail = mail.replace(secret_mail, len(secret_mail) * '*')
print(secret_mail)



    
# #Завдання 3-Додавання унiкального значення з використанням list для створення свого set()

numbers = [1,2,3,4,5]

user_num = int(input("Введiть будь яку цифру: "))


if user_num in numbers:
    print ("Таке число вже э")
else:
    numbers.append(user_num)
    print(f"Ось новий список з вашою допомогою {numbers} ")
        



# #Завдання 4-Аналiз тегiв i персональних iнтересiв кожного юзера

first_user_interests = input(f"Введiть будь ласка у виглядi тегiв через кому,\n Наприклад: ai, python, music, war\n")
second_user_interests = input(f"\nВведiть будь ласка у виглядi тегiв через кому,\n Наприклад: ai, python, music, war\n")

first_user_tags = set()
second_user_tags = set()

first_user_tags.update((first_user_interests.strip()).split(","))
second_user_tags.update((second_user_interests.strip()).split(","))

print(f"Теги першого юзера: {first_user_tags}")
print(f"Теги другого юзера: {second_user_tags}")

print(f"Спiльнi iнтереси: {first_user_tags.intersection(second_user_tags)}")

print(f"Унiкальнi iнтереси для першого юзера: {" ,".join(first_user_tags.difference(second_user_tags))}\n" )
print(f"Унiкальнi iнтереси для другого юзера: {" ,".join(second_user_tags.difference(first_user_tags))}\n")





# #Завдання 5-Обробка рядка з числами
user_nums_for_sum = input("Введiть значення для суми всiх вказених чисел(вводити через пробiл): ")
numbers_list = user_nums_for_sum.split()

numbers_sum = 0
for number in numbers_list:
    if number.isdigit():
        numbers_sum += int(number)
    else:
        print(f"{number}- не є числом")
        
print(f"Сумою усiх ваших чисел = {numbers_sum}")


