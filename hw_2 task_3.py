# Задача_ 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input("Введите норем месяца (от 1 до 12): "))

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'Winter',
                2: 'Spring',
                3: 'Summer',
                4: 'Autumn'}

if month == 1 or month == 12 or month == 2:
    print(seasons_list[0])
    print(seasons_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
    print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
    print(seasons_dict.get(4))
else:
    print("Ошибка! Нет такого месяца!")


month = int(input("Введите номер месяца (от 1 до 12): "))
seasons_dict = {'Winter': (1, 2, 12),
                'Spring': (3, 4, 5),
                'Summer': (6, 7, 8),
                'Autumn': (9, 10, 11)}
for key in seasons_dict.keys():
    if month in seasons_dict[key]:
        print(key)
