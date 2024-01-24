# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform


##############################################################################
# file = open('file.txt', 'a', encoding='utf-8')
# file.write(input('Введите строку для записи: ' + '\n'))
# file.close()
# # Чтоб не писать лишние close и др, используем контекстный менеджер:
#
# with open('file.txt', 'a', encoding='utf-8') as file:
#     file.write(input('Введите строку для записи: ' + '\n'))
# print(file) # В этом случае команда close выполняется автоматически
#######################################################################################
# Для минимального и максимального значений вводим константы:
MIN_LIMIT = -1000
MAX_LIMIT = 1000


# Создаем функцию write_numbers, которая получает на вход имя файла (file_name) в виде строки,
# количество строк (count). Возвращать функция ничего не будет.
def write_numbers(file_name: str, count: int):
    with open(file_name, 'a', encoding='UTF-8') as file:
        for _ in range(count):
            #   file.write(randint(MIN_LIMIT,MAX_LIMIT) + '|' + uniform(MIN_LIMIT,MAX_LIMIT)) # Так не пойдет,так как
            # инт через палку с флоатом (uniform) не запишется. Поэтому все это переводим в строку:
            # file.write(str(randint(MIN_LIMIT,MAX_LIMIT)) + '|' + str(uniform(MIN_LIMIT,MAX_LIMIT))) # или так:
            file.write(f'{randint(MIN_LIMIT, MAX_LIMIT)} | {uniform(MIN_LIMIT, MAX_LIMIT)}\n')


write_numbers('nums.txt', 10)  # Создаем файл nums.txt и выведем 10 строк пар случайных чисел
