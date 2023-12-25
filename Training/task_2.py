# Задача 2
# Необходимо удалить пустые строки из списка строк

my_list = ['one', 'two', '', 'three', '', 'for']
resList = list(filter(None, my_list)) # Мы можем использовать функцию filter()
# для удаления объектов типа None из списка
print(resList)