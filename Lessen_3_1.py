# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_del(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return ('На ноль делить нельзя')


def my_del_1(a, b):
    if b == 0:
        print ('На ноль делить нельзя')
    return a / b


def my_del_2():
    a = int(input('Введите первое число'))
    b = int(input('Введите второе число'))
    try:
        return a / b
    except ZeroDivisionError:
        return ('На ноль делить нельзя')

print (my_del(10, 0))
print (my_del_1(10, 5))
print (my_del_2())