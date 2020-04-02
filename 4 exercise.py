#done
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
_digit = abs(int(input('Введите положительное целое число : ')))
_cou_digit = 0
_temp = _digit
_max = _digit % 10
i = 0
while _temp > 0:
    _temp //= 10
    _cou_digit += 1
print(f'Количество знаков в числе: {_cou_digit}')

while _cou_digit > i:
    _digit //= 10
    if _max == 9:
        print(_max)
        break
    elif _digit % 10 > _max:
        _max = _digit % 10
        i += 1
    else:
        i += 1
print(f'Большее число = {_max}')
