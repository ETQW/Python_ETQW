'''6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.'''

from itertools import count, cycle
#a
i = 'h'
for el in count(int(input('Введите стартовое число '))):
    if i == 'q' or i == 'Q':
        break
    else:
        print(el)
    print('Для выхода введи q')
    i = input()
#b
#Одновременне только одно условие будет работать ( второе- коментировать
my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    if i == 'q' or i == 'Q':
        break
    else:
        print(el)
    print('Для выхода введи q')
    i = input()
