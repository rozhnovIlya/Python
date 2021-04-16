# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
my_file = open('task_2.txt', 'r')
string = my_file.read()
print(f'Содержимое файла:\n{string}')
my_file = open('task_2.txt', 'r')
string = my_file.readlines()
print(f'Количество строк в файле - {len(string)}')
my_file = open('task_2.txt', 'r')
string = my_file.readlines()
for i in range(len(string)):
    print(f'Кличество символов {i + 1} - ой строки {len(string[i])}')
my_file = open('task_2.txt', 'r')
string = my_file.read()
string = string.split()
print(f'Общее количество слов - {len(string)}')
my_file.close()