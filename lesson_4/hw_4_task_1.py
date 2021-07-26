# Задача_1 (дз_4). Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, production_hours, rate_hour, bonus = argv

print(f'Имя скрипта: {script_name}')
print(f'Выработка в часах: {production_hours}')
print(f'Ставка в часах: {rate_hour}')
print(f'Премия: {bonus}')

wages_calculation = ((int(production_hours) * int(rate_hour)) + int(bonus))

print(f'Заработная плата равна: {wages_calculation}')
