# Задача_1 (ДЗ_8). Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data(object):

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, data_as_string):
        day, month, year = map(int, data_as_string.split('-'))
        data = cls(day, month, year)
        return data

    @staticmethod
    def is_data_valid(data_as_string):
        day, month, year = map(int, data_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


data = Data.from_string('19-11-2019')
is_data = Data.is_data_valid('19-11-2019')
print(data)
print(is_data)
