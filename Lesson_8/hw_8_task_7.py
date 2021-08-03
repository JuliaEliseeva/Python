# Задача_7 (ДЗ_8). Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, numb_1, numb_2):
        self.numb_1 = numb_1
        self.numb_2 = numb_2

    def __add__(self, other):
        return f'Сумма равна: {self.numb_1 + other.numb_1} + {self.numb_2 + other.numb_2} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.numb_1 * other.numb_1 - (self.numb_2 * other.numb_2)} ' \
               f'+ {self.numb_2 * other.numb_1} * i'


n_1 = ComplexNumber(6, -6)
n_2 = ComplexNumber(8, 13)
print(n_1 + n_2)
print(n_1 * n_2)
