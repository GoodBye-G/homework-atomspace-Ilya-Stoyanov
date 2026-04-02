# #Завдання 1 -Iнiцiали

# name=str(input("Введiть своє iм`я ты прiзвище(Name Surname)"))
# initials=[]

# #Тут ми робимо з iменi список (name.split) i перебираємо першi лiтери з кожного члена списку(iм`я та прiзвище)
# for word in name.split():
#     initials.append(word[0]) #додаємо у пустий список першу букву з кожного члена списку

# #перевiрка на iм`я`
# if not name:
#     print("Перевiрте написане iм`я")
# else:
#     #метод .join щоб зробити з списку назад рядок (str)
#     print(f"Все добре вот ваши iнiцiали: {" ".join(initials)}")






# #Завдання 2 -Маскування email
# mail=input("Введiть свою електрону пошту: ")

# #перевiряю на окiнчення пошти
# if mail[-4:] != ".com" and mail[-4:] != ".org":
#     print("Пошта не закiнчується на .org та .com")
# elif not mail:
#     print("Напешiть будь ласка пошту")
# else:
#     pass

# # com потрiбен щоб порахувати яким є по рахунку символ "@"
# com=0
# for letters in mail:
#     if letters != "@":
#         com=com+1
#     else:
#         break

# #Замiнюю (.replace) пошту на "*" окрiм першого, останнбого символу та домену
# secret_mail=mail[1:com-1]
# secret_mail=mail.replace(secret_mail, len(secret_mail) * '*')
# print(secret_mail)



    
# #Завдання 3-Додавання унiкального значення
# numbers={1,2,3,4,5}

# new_num=int(input("Введiть будь яку цифру: "))

# #Використовую цикл щоб пройтись по кожному значеннi в множинi та перевiрити чи є воно там, якщо є повiдомляю користувача що вже є
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

# #Пуста множина
# tags_1=set()
# tags_2=set()

# #"Вичищаю" теги юзера вiд пробiлiв та роблю з строки список з роздiлом через коми--> потiм додаю в пусту множину
# tags_1.update((user_1.strip()).split(","))
# tags_2.update((user_2.strip()).split(","))

# print(f"Теги першого юзера: {tags_1}")
# print(f"Теги другого юзера: {tags_2}")

# print(f"Спiльнi iнтереси: {tags_1.intersection(tags_2)}")

# #Дивлюсь унiкальнi iнтереси кожного юзера i результат вивожу строкою
# print(f"Унiкальнi iнтереси для першого юзера: {" ,".join(tags_1.difference(tags_2))}\n" )
# print(f"Унiкальнi iнтереси для другого юзера: {" ,".join(tags_2.difference(tags_1))}\n")





# #Завдання 5-Обробка рядка з числами
numbers=input("Введiть значення для суми всiх вказених чисел(вводити через пробiл): ")
numbers_list=numbers.split()



element=0; sum=0; count=0
for num in range(len(numbers_list)):    #Ми проходимось по кожному числу(члену списку)
    element=numbers_list[num]
    if element.isdigit():               #Якщо число є int то йдеме далi
        sum+=int(element)               #Це сумма чисел якi доходять до цього моменту в циклi 
        count+=1                        #count нам потрiбен щоб в суму не входило бiльше трьох членiв
        if count==3:                    #3 члена --> кiнець
            break        
    else:                               #На той випадок якщо користувач вiв не число
        print(f"{element}- НЕ є числом")

print(f"Сума перших трьох членiв{sum}")


