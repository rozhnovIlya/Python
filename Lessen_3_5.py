
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа разделеные пробелом, для выхода нажмите Q - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма равна {sum_res}')
    print(f'Конечная сумма равна {sum_res}')
my_sum()