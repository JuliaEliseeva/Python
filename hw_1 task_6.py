# Задача_6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.

a = float(input("Введите результат пробежки в первый день: "))
b = float(input("Введите общий желаемый результат: "))
day = 1

while a < b:
    a = a * 1.1
    day += 1

print(f"Общий желаемый результат будет достигнут на %.d день" % day)