'''Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.'''

my_str = 'aasjasjdasdasdas'
my_dict = ({char:ord(char) for char in my_str})
print(my_dict)

'''Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итератор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.'''
#my_dict = {'j': 106, 'd': 100, 'k': 107, 'v': 118, 'n': 110, 'e': 101, 't': 116, 'g': 103, 'l': 108}
it_dict = iter(my_dict.items())
for i in range(5):
    print(next(it_dict))