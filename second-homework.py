# #Завдання 1 -Iнiцiали

# name=str(input("Введiть своє iм`я ты прiзвище(Name Surname)"))
# initials=[]

# for word in name.split():
#     initials.append(word[0]) #додаємо у пустий список першу букву з кожного члена списку

# if not name:
#     print("Перевiрте написане iм`я")
# else:
#     #метод .join щоб зробити з списку назад рядок (str)
#     print(f"Все добре вот ваши iнiцiали: {" ".join(initials)}")






# #Завдання 2 -Маскування email
# mail=input("Введiть свою електрону пошту: ")

# if mail[-4:] != ".com" and mail[-4:] != ".org":
#     print("Пошта не закiнчується на .org та .com")
# elif not mail:
#     print("Напешiть будь ласка пошту")
# else:
#     pass

# com=0
# for letters in mail:
#     if letters != "@":
#         com=com+1
#     else:
#         break

# secret_mail=mail[1:com-1]
# secret_mail=mail.replace(secret_mail, len(secret_mail) * '*')
# print(secret_mail)



    
# #Завдання 3-Додавання унiкального значення
# numbers={1,2,3,4,5}

# new_num=int(input("Введiть будь яку цифру: "))

# for num in numbers:
#     if num==new_num:
#          print(f"Таке значення вже є, ось як виглядає список: {numbers}")       
#          break    
        
# else:
#         numbers.add(new_num)
#         print(f"Ось так виглядає новик список з вашою допомогою: {numbers}")
        






# #Завдання 4-Аналiз тегiв
# user_1=input(f"Введiть будь ласка у виглядi тегiв через кому,\n Наприклад: ai, python, music, war\n")
# user_2=input(f"\nВведiть будь ласка у виглядi тегiв через кому,\n Наприклад: ai, python, music, war\n")

# tags_1=set()
# tags_2=set()

# tags_1.update((user_1.strip()).split(","))
# tags_2.update((user_2.strip()).split(","))

# print(f"Теги першого юзера: {tags_1}")
# print(f"Теги другого юзера: {tags_2}")

# print(f"Спiльнi iнтереси: {tags_1.intersection(tags_2)}")

# print(f"Унiкальнi iнтереси для першого юзера: {" ,".join(tags_1.difference(tags_2))}\n" )
# print(f"Унiкальнi iнтереси для другого юзера: {" ,".join(tags_2.difference(tags_1))}\n")





# #Завдання 5-Обробка рядка з числами
# numbers=input("Введiть значення для суми всiх вказених чисел(вводити через пробiл): ")
# numbers_list=numbers.split()



# element=0; sum=0; count=0
# for num in range(len(numbers_list)):   
#     element=numbers_list[num]
#     if element.isdigit():               
#         sum+=int(element)               
#         count+=1                        
#         if count==3:                    
#             break        
#     else:                               
#         print(f"{element}- НЕ є числом")

# print(f"Сума перших трьох членiв{sum}")



