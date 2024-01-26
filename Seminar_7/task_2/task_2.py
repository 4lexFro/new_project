# Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random
from random import randint, choice

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']


def gen_name():
    MIN = 4
    MAX = 7
    name_len = randint(MIN, MAX)
    rand_name = ''
    is_vowels = False
    for i in range(name_len):
        dict_choice = randint(0, 1)
        if dict_choice:
            is_vowels = True
        rand_name += random.choice(vowels) if dict_choice else random.choice(consonants)
    if not is_vowels:
        rand_name += 'a'
    return (rand_name.capitalize())


def write_names(count: int):
    with open('names.txt', 'a', encoding='UTF-8') as f:
        for _ in range(count):
            f.write(gen_name() + '\n')
write_names(4)
