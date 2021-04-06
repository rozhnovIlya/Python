# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

values_str =  input('Введите значения списка')
values = list (values_str)
counter = 0
for el in range(len(values) // 2):
    values[counter], values[counter+1] = values[counter+1], values[counter]
    counter = counter + 2
print(values)

