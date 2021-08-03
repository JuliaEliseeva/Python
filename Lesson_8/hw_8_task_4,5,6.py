# Задача_4 (ДЗ_8). Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Задача_5 (ДЗ_8). Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# Задача_6 (ДЗ_8). Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, year, colour):
        self.name = name
        self.year = year
        self.colour = colour
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.year} {self.colour}'


class Printer(Equipment):
    def __init__(self, name, year, colour, series):
        super().__init__(name, year, colour)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.year} {self.colour} {self.series}'

    def act(self):
        return 'Печатает'


class Scanner(Equipment):
    def __init__(self, name, year, colour, model):
        super().__init__(name, year, colour)
        self.model = model

    def __repr__(self):
        return f'{self.name} {self.year} {self.colour} {self.model}'

    def act(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, year, colour, weight):
        super().__init__(name, year, colour)
        self.weight = weight

    def __repr__(self):
        return f'{self.name}  {self.year} {self.colour} {self.weight}'

    def act(self):
        return 'Копирует'


warehouse = Warehouse()
scan_1 = Scanner('HP', 2015, 'white', '321-e')
warehouse.add_to(scan_1)
scan_2 = Scanner('Sony', 2010, 'black', '290-u')
warehouse.add_to(scan_2)
scan_3 = Scanner('HP', 2018, 'red', '330-e')
warehouse.add_to(scan_3)
print(scan_1)
print(scan_2)
print(scan_3)
p_1 = Printer('Canon', 2000, 'green', '2590-t')
warehouse.add_to(p_1)
p_2 = Printer('Samsung', 2020, 'white', '3809-e')
warehouse.add_to(p_2)
p_3 = Printer('Brother', 2021, 'black', '4906-p')
warehouse.add_to(p_3)
print(p_1)
print(p_2)
print(p_3)
x_1 = Xerox('Xerox', 2018, 'white', '2,5 kg')
warehouse.add_to(x_1)
x_2 = Xerox('HP', 2016, 'white', '3,5 kg')
warehouse.add_to(x_2)
x_3 = Xerox('Sony', 2010, 'black', '4,5 kg')
warehouse.add_to(x_3)
print(x_1)
print(x_2)
print(x_3)
print(warehouse.__dict__)
print(warehouse._dict)
print(warehouse._dict)

print(scan_2.act())
print(p_1.act())
print(x_3.act())
