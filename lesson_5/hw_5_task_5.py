# Задача_5 (ДЗ_5). Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def my_sum():
    try:
        with open('task_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            my_numbers = line.split()

            print(sum(map(int, my_numbers)))
    except IOError:
        print('Ошибка в файле!')
    except ValueError:
        print('Ошибка ввода-вывода данных!')


my_sum()
