# Задача_4 (ДЗ_6). Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля: {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной!'
        else:
            return f'Скорость {self.name} допустима'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля: {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает разрешенную!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из отдела полиции'
        else:
            return f'{self.name} не относиться к полиции'


l = SportCar(100, 'Желты', 'Lamborghini', False)
k = TownCar(90, 'Зеленый', 'Kia', False)
lada = WorkCar(70, 'Белый', 'Lada', True)
f = PoliceCar(110, 'Синий', 'Ford', True)
print(l.name)
print(l.is_police)
print(l.color)
print(l.turn_left())
print(l.stop())
print(k.name)
print(k.is_police)
print(k.color)
print(k.show_speed())
print(k.turn_left())
