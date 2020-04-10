'''2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.'''


def authority(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])


print(authority(name='Захар', surname='наЗОЖЕ', year='1995', city='Суздаль', email='god_like@mail.bk',
                phone='+7(915)2354875'))
