# Задача 1
# Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует,
# замените его на 200. Обновите список только при первом вхождении числа 20.

my_list = [1, 3, 20, 45, 24, 76, 20, 8, 23]
index = my_list.index(20)
print(index)
my_list[index] = 200
print(my_list)
