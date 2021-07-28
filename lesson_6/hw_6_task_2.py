# Задача_2 (ДЗ_6). Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, thickness):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.thickness = thickness

    def mass(self):
        my_length = self._length
        my_width = self._width
        my_weight = self.weight
        my_thickness = self.thickness
        total = my_length * my_width * my_weight * my_thickness / 1000
        return print(f"Масса асфальта\n {my_length}м * {my_width}м * {my_weight}кг * {my_thickness}см = ", int(total),
                     "т")


r = Road(20, 5000, 25, 5)
r.mass()
