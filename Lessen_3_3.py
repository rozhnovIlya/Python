# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func():
    a = int(input('Введите число'))
    b = int(input('Введите число'))
    c = int(input('Введите число'))
    list = [a, b, c]
    max_1 = max(list)
    list.remove(max_1)
    max_2 = max(list)
    return sum(max_1 + max_2)
print(f"Сумма двух максимальных аргументов равна - {my_func()}")



