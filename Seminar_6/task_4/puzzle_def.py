# 📌 Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# 📌 Ключ словаря - загадка, значение - список с отгадками.
# 📌 Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.


# import random
from random import randint, choice


def puzzle(puzzle_txt: str, variant: list[str], tries: int) -> int:
    print(puzzle_txt)
    variant_v = list(map(lambda x: x.lower(), variant))
    num = 0
    while num < tries:
        user_input = input('введите вариант ответа: ').lower()
        if user_input in variant_v:
            num += 1
            return num
        else:
            print('не угадали!')
        num += 1
    return 0


# def puzzle_solut():
#     dict_puzzle = {
#         'Зимой и летом одним цветом': ['ель', 'пихта', 'сосна'],
#         'Висит груша - нельзя скушать!': ['лампа', 'лампочка'],
#         'Не лает,не кусает,в дом не пускает': ['замок', 'ключ']
#     }
#
#     for key, values in dict_puzzle.items():
#         puzzle(key, values, random.randint(1, 3))

# Вариант препода:

def puzzle_solut():
    dict_puzzle = {
        'Зимой и летом одним цветом': ['ель', 'пихта', 'сосна'],
        'Висит груша - нельзя скушать!': ['лампа', 'лампочка'],
        'Не лает,не кусает,в дом не пускает': ['замок', 'ключ']
    }

    for _ in range(len(dict_puzzle)):
        cur_puzzle = choice(list(dict_puzzle))
        cur_value = dict_puzzle.pop(cur_puzzle)
        puzzle(cur_puzzle, cur_value, randint(1, 3))

