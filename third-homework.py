#calculator

stop_signal=0
while stop_signal != -90:
        first_num_for_operation = int(input("Введiть перше число для опрацьовування: "))
        second_num_for_operation = int(input("Введiть друге число для опрацьовування: "))

        operation = input("Яку операцiї ви бажаєте здiйснити(+, -, *, /, **): ")

        if operation == "+":
              print (first_num_for_operation + second_num_for_operation)
        elif operation == "-":
              print (first_num_for_operation - second_num_for_operation)
        elif operation == "*":
              print (first_num_for_operation * second_num_for_operation)
        elif operation == "/":
              print (first_num_for_operation / second_num_for_operation)
        elif operation == "**":
              print (first_num_for_operation ** second_num_for_operation)
        else:
              print("Invalid operation")
        stop_signal = int(input("Якщо ви бажаєте припинити програму введiть '-90' "))

              


#витрати за категорiями

users_balance = float(input("Введiть свiй початковий баланс: "))

spends_balance = {

}


stop_signal = 0
while stop_signal != "exit":
    purchase_category = (input("Введiть котигорiю покупок(Наприклад технiка): ")).strip().lower()
    purchase_money = float(input("Введiть скiльки грошей ви витратили в цiй категорiї: "))

    if users_balance <= 0:
          print("Вашего баланса недостатньо для проведення операцiї: ")
    else:
       users_balance -= purchase_money
       spends_balance[purchase_category] = spends_balance.get(purchase_category , 0) + purchase_money
       print(spends_balance)
       
       stop_signal = input("Введiть 'exit' щоб вийти з циклу: ")



    




