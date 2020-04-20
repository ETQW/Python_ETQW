'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.'''


class Car:
    # Определим атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # Определим методы
    def go(self):
        return f'{self.name} Поехала'

    def stop(self):
        return f'{self.name} Остановилась'

    def turn_right(self):
        return f'{self.name} Свернула направо'

    def turn_left(self):
        return f'{self.name} Свернула влево'

    def turn_over_crossroad(self):
        return f'{self.name} Развернулась на перекрестке'

    def show_speed(self):
        return f'Сейчас автомобиль {self.name} движится со скоростью {self.speed}'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Сейчас автомобиль {self.name} движится со скоростью {self.speed}')

        if self.speed >= 40:
            return f'Авто  {self.name} превысил скорость для движения по рабочим нуждам'
        else:
            return f'Скорость авто {self.name} норма!'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Сейчас автомобиль {self.name} движится со скоростью {self.speed}')

        if self.speed >= 60:
            return f'Авто  {self.name} превысил скорость для движения по городу'
        else:
            return f'Скорость авто {self.name} норма!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            if self.speed >= 60:
                return f'Мы ж из полиции, А что вы хотели! спешим за пончиками? гоним {self.speed} км/ч'
            else:
                return f'Мы из полиции (( Опять работать... поехали  не быстрее {self.speed} км/ч'
        else:
            return f'Авто {self.name} не полицейская тачила'



Dodge_viper = SportCar(120, 'white/blue', 'Dodge viper', False)
oka = TownCar(40, 'Red', 'Oka', False)
hyundai = TownCar(90, 'Pink', 'hyundai', False)
vaz = WorkCar(70, 'White', 'vaz', False)
ford = PoliceCar(290, 'Blue', 'Ford', True)
bmv = PoliceCar(20, 'Black', 'BMV', True)
print(vaz.turn_left())
print(
    f'Когда {hyundai.turn_over_crossroad()}, тогда {bmv.go()} со скоростью {bmv.show_speed()}, а в это время {Dodge_viper.stop()}')
print(f'{Dodge_viper.go()} на скорости {Dodge_viper.show_speed()}')
print(f'{vaz.name} цвета {vaz.color}')
print(f'А коп ли {Dodge_viper.name} ? {Dodge_viper.is_police}')
print(f'А коп ли {ford.name}  ? {ford.is_police}')
print(bmv.police())
print(bmv.show_speed())
print(Dodge_viper.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
