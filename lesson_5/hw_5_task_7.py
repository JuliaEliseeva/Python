# Задача_7 (ДЗ_5). Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

my_income = {}
pr = {}
income = 0
aver_income = 0
i = 0
with open('task_7.txt', 'r') as file:
    for line in file:
        name, firm, profit, costs = line.split()
        my_income[name] = int(profit) - int(costs)
        if my_income.setdefault(name) >= 0:
            income = income + my_income.setdefault(name)
            i += 1
    if i != 0:
        aver_income = income / i
        print(f'Прибыль средняя: {aver_income:.2f}')
    else:
        print(f'Прибыль средняя: отсутсвует. Все работают в убыток')
    pr = {'Средняя прибыль': round(aver_income)}
    my_income.update(pr)
    print(f'Прибыль каждой компании: {my_income}')

with open('hw5_task_7.json', 'w') as write_js:
    json.dump(my_income, write_js)

    js_str = json.dumps(my_income)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
