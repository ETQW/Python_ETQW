'''7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.'''


class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'новый z = {self.a + other.a} + {self.b + other.b}*i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'новый z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + (self.a * other.b)}*i'

    def __str__(self):
        return f'z = {self.a} + {self.b}*i'


z_1 = ComplexNum(2, -3)
print(f'z1 ={z_1}')
z_2 = ComplexNum(1, 1)
print(f'z1 ={z_2}')
print(z_1 + z_2)
print(z_1 * z_2)
