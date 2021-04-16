# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open('my_file.txt', 'w')
string = input('Введите данные файла')
while string:
    my_file.writelines(string)
    string = input('Введите данные файла')
    if not string:
        break
my_file.close()
my_file = open('my_file.txt', 'r')
data = my_file.readlines()
print(data)
my_file.close()
