# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

from itertools import count

from itertools import cycle

starting_number = int(input('Введите стартовое число'))
final_number = int(input('Введите конечное число'))
for el in count(starting_number):
    if el > final_number:
        break
    else:
        print(el)

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    if starting_number > final_number:
        break
    print(el)
    starting_number += 1