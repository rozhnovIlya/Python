#Запросите у пользователя значения выручки и издержек фирмы. Определите,
#с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или
#убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с
#прибылью, вычислите рентабельность выручки
#(соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и
#определите прибыль фирмы в расчете на одного сотрудника

revenue = int(input("Введите размер выручки"))
costs = int(input("Введите размер издержек"))
if revenue > costs:
    print("Прибыль,", (revenue - costs),"рентабильность составила,", ((revenue - costs) / revenue)*100)
    personal = int(input("Введите количество сотрудников"))
    print("Прибыль на одного сотрудника составила,", ((revenue - costs) / personal))
if revenue <= costs:
    print("Убыток!")


