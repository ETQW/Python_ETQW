# -*- coding: cp1251 -*-
'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''


def summa():
    try:
        with open('test5.txt', 'w+') as f:
            line = input('Запишите цифры через пробел \n')
            f.writelines(line)
            num = line.split()

            s_sum =(sum(map(int, num)))
            line = f'\nСумма = {s_sum}'
            f.writelines(line)
            print(f'Сумма = {s_sum}')
    except ValueError:
        print('Введено точно не число!')


summa()
