# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


# def fun_salary ():
#     time = int(input('Введите отработанное количество часов '))
#     rate = int(input('Введите размер ставки '))
#     bonus = int(input('Введите размер премии '))
#     salary = (time * rate) + bonus
#     return print(f'Заработная плата составила - {salary}')
# fun_salary()

new, time, rate, bonus = argv
time = int(time)
rate = int(rate)
bonus = int(bonus)
salary = time * rate + bonus
print(f'Заработная плата составила - {salary}')


