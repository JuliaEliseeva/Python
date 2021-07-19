# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_function(surname, name, year, city, email, telephone):
    return ' '.join([surname, name, year, city, email, telephone])


print(
    f'{input("Фамилия: ")}, {input("Имя: ")}, {input("Год рождения: ")}, {input("Город прожвания: ")}, {input("Email: ")}, {input("Номер телефона: ")}')


def my_func(name, surname, year, city, email, telephone):
    print(surname, name, year, city, email, telephone)


my_func(surname='Смирнов', name='Алексей', year='1992', city='Киров', email='smirnov92@yandex.ru',
        telephone='342-60-98')
