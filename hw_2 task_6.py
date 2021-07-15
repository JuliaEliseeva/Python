# Задача_6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {“название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]}

goods = []
features_goods = {'Название': '', 'Цена': '', 'Количество': '', 'ед': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'ед': []}
num = 0
feature = None
control = None

while True:
    control = input("Для выхода нажмите 'D', для продолжения нажмите 'Enter', для анализа нажмите 'B'").upper()
    if control == 'D':
        break
    num += 1
    if control == 'B':
        for key, value in analytics.items():
            print(f'{key}: {value}')
    for f in features_goods.keys():
        feature = input(f'Введите "{f}"')
        features_goods[f] = int(feature) if (f == 'Цена' or f == 'Количество') else feature
        analytics[f].append(features_goods[f])
    goods.append((num, features_goods))


# goods = int(input("Введите количество товара "))
# n = 1
# my_dict = []
# my_list = []

# while n <= goods:
#   my_dict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
#                   'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
#    my_list.append((n, my_dict))
#    n += 1

# print(my_list)