# Вы получаете массив чисел, возвращаете сумму всех положительных чисел.
#
# Пример [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Примечание. Если суммировать нечего, сумма по умолчанию равна 0.
# def positive_sum(arr):
#     new_arr = []
#     for el in arr:
#         if el >= 0:
#             new_arr.append(el)
#     new_sum = sum(new_arr)
#     if new_sum == 0:
#         return 0
#     else:
#         return new_sum

# Или так:

def positive_sum(arr):
    return sum(x for x in arr if x > 0)
arr = [-2,4,6,4]
print(positive_sum(arr))