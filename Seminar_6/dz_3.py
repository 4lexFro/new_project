# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте
# различный случайные варианты и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на
# шахматной доске, в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом,
# что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
# Пример использования На входе:
#print(generate_boards())


# На выходе:
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)], [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)], [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)], [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]
from random import randint
def is_attacking(q1: tuple, q2: tuple):
    x1, y1 = q1
    x2, y2 = q2
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    return False


def check_queens(queens: list):
    for i in range(len(queens) - 1):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True

#print(check_queens(queens))

def generate_boards():
    board_list = []
    while len(board_list) < 4:
        test_set = []
        while len(test_set) < 8:
            if not test_set:
                test_set.append((randint(1,9),randint(1,9)))
            x,y = randint(1,9), randint(1,9)
            if not is_attacking(test_set[-1], (x,y)):
                test_set.append((x,y))
        if check_queens(test_set):
            board_list.append(test_set)
    return board_list


print(generate_boards())
