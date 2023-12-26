# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# Пример:
# На входе:

#lst = [1, 1, 2, 2, 3, 3]
lst = [1, 'one', True, 'one', 3, 'peter', True, 23, 3, 23, 'peter']

# На выходе:
#
# [1, 2, 3]
lst_res = []
for item in lst:
    if lst.count(item) > 1 and item not in lst_res:
        lst_res.append(item)
print(lst_res)
