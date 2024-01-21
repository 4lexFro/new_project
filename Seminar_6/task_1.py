# Создайте модуль с функцией внутри.
# 📌 Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# 📌 Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# 📌 Функция выводит подсказки “больше” и “меньше”.
# 📌 Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

from random import randint as rand


# def game(low: int, up: int, count: int):
#     result = False
#     count_try = 0
#     number = rand(low, up)
#     while count_try < count:
#         variant = int(input('Введите ваш вариант числа :'))
#         if variant < number:
#             print('Загаданное число больше!')
#         elif variant > number:
#             print('Загаданное число меньше!')
#         else:
#             result = True
#             break
#         count_try += 1
#     return result
#
#
# print(game(1, 10, 3))

# Вариант препода:

def game(low: int=1, up: int=100, count: int=6):
    number = rand(low, up)
    while count:
        variant = int(input('Введите ваш вариант числа :'))
        if variant < number:
            print('Загаданное число больше!')
        elif variant > number:
            print('Загаданное число меньше!')
        else:
            print('Вы угадали!')
            return True
        count -= 1
    print(f'Увы... Было загадано число {number}')
    return False

    if __name__ == '__main__':
        print(game(1, 10, 3))
