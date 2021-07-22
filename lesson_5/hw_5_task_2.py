# Задача_2 (ДЗ_5). Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task_2.txt', 'r', encoding="utf-8") as file:
    my_list = file.readlines()
    for i in range(len(my_list)):
        new_list = my_list[i].split()
        print(f'В {i + 1}-ой строке - {len(new_list)} слов(o/а)')

print(f"Количество слов в файле: {len(my_list)}")
