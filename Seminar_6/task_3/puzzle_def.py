# Создайте модуль с функцией внутри.
# 📌 Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# 📌 Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.
def puzzle(puzzle_txt:str, variant: list[str], tries: int) -> int:
    print(puzzle_txt)
    variant_v = list(map(lambda x: x.lower(),variant))
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








