# -*- coding: cp1251 -*-
'''5. ������� (����������) ��������� ����, �������� � ���� ���������� ����� �����, ����������� ���������.
��������� ������ ������������ ����� ����� � ����� � �������� �� �� �����.'''


def summa():
    try:
        with open('test5.txt', 'w+') as f:
            line = input('�������� ����� ����� ������ \n')
            f.writelines(line)
            num = line.split()

            s_sum =(sum(map(int, num)))
            line = f'\n����� = {s_sum}'
            f.writelines(line)
            print(f'����� = {s_sum}')
    except ValueError:
        print('������� ����� �� �����!')


summa()
