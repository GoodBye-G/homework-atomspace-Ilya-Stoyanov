#calculator

while True:
        first_num = int(input("Введiть перше число для опрацьовування: "))
        second_num = int(input("Введiть друге число для опрацьовування: "))

        operation = input("Яку операцiї ви бажаєте здiйснити(+, -, *, /, **): ")

        if operation == "+":
              print(first_num + second_num)
        elif operation == "-":
              print(first_num - second_num)
        elif operation == "*":
              print(first_num * second_num)
        elif operation == "/":
              if second_num != 0:
                print(first_num / second_num)
              else:
                print("На 0 дiлити заборонено")

        elif operation == "**":
              print(first_num ** second_num)
        else:
              print("Invalid operation")
        stop_signal = input("введiть 'exit' для виходу з програми: ")
        if stop_signal == "exit":
              break

              


#витрати за категорiями

user_balance = float(input("Введiть свiй початковий баланс: "))

spends_balance = {}


stop_signal = 0
while True:
    category = (input("Введiть котигорiю покупок(Наприклад технiка): ")).strip().lower()
    amount = float(input("Введiть скiльки грошей ви витратили в цiй категорiї: "))

    if user_balance <= 0:
          print("Вашего баланса недостатньо для проведення операцiї: ")
    else:
       if user_balance >= amount:
        user_balance -= amount
        spends_balance[category] = spends_balance.get(category , 0) + amount
        print(spends_balance)
       else:
           print("Недостатньо коштiв для проведення операцiї")
       
       stop_signal = input("Введiть 'exit' щоб вийти з циклу: ")
       if stop_signal == "exit":
           break



    




