# Задача_3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3


print(
    f'{my_func(float(input("Введите аргумент №1: ")), float(input("Введите аргумент №2: ")), float(input("Введите аргумент №3: ")))}')
