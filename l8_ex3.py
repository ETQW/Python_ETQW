'''3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.'''


class myerror(Exception):
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            val = input('Введите численное значение и нажимайте Enter - ')
            try:
                val = int(val)
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Введена строка или недопустимый символ.")
                chose = input(f'Попробовать еще раз? Y/N ')
                if chose == 'Y' or chose == 'y':
                    print(try_except.my_input())
                elif chose == 'N' or chose == 'n':
                    return f'Вы вышли'
                    break
                else:
                    print(f"Введены не Y или N.")
                    chose = input(f'Попробовать еще раз? Y/N ')


try_except = myerror(1)
print(try_except.my_input())
