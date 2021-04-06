# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
season_list = ['Зима', 'Весна', 'Лето', 'Осень']
mouth = int(input('Введите номер месяца '))

if mouth == 12 or mouth == 1 or mouth == 2:
    print (season_dict.get(1))
    print (season_list[0])
elif mouth == 3 or mouth == 4 or mouth == 5:
        print (season_dict.get(2))
        print (season_list[1])
elif mouth == 6 or mouth == 7 or mouth == 8:
        print (season_dict.get(3))
        print (season_list[2])
elif mouth == 9 or mouth == 10 or mouth == 11:
        print (season_dict.get(4))
        print (season_list[3])
else:
    print ('Нет такого месяца')


