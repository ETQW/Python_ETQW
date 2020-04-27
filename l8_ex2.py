'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class zerodivide:
    def __init__(self, num1, num2):
        self.divider = num1
        self.denominator = num2

    @staticmethod
    def divide_by_null(num1, num2):
        try:
            return (num1 / num2)
        except:
            return (f"Нельзя просто так взять и поделить на 0!")


div = zerodivide(25, 5)
print(zerodivide.divide_by_null(25, 5))
print(zerodivide.divide_by_null(32, 0))
print(zerodivide.divide_by_null(40, 5))
print(div.divide_by_null(124245, 0))
