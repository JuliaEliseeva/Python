# Задача_2 (ДЗ_7). Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Textile:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_coat_sq(self):
        return self.size / 6.5 + 0.5

    def get_costume_sq(self):
        return self.height * 2 + 0.3

    @property
    def full_sq(self):
        return str(f'Общая площадь затраченной ткани: {(self.get_coat_sq()) + (self.get_costume_sq())}')


class Coat(Textile):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.sq_coat = round(self.get_coat_sq())

    def __str__(self):
        return f'Площадь затраченной ткани на пальто: {self.sq_coat}'


class Jacket(Textile):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.sq_costume = round(self.get_costume_sq())

    def __str__(self):
        return f'Площадь затраченной ткани на костюм: {self.sq_costume}'


t = Textile(46, 170)
print(t.full_sq)
print(t.get_coat_sq())
print(t.get_costume_sq())

