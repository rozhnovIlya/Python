#Пользователь вводит целое положительное число.Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
number = int(input("Введите число"))
number_max = number % 10
number = number // 10
while number > 0:
    if number % 10 > number_max:
        number_max = number % 10
    number = number // 10
print(number_max)




