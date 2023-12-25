# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки. ✔Строки нумеруются
# начиная с единицы. ✔Слова выводятся отсортированными согласно
# кодировки Unicode. ✔Текст выравнивается по правому краю так,
# чтобы у самого длинного слова был один пробел между ним и
# номером строки.
text = "hello beautiful world"
def text_method(str: text):
    my_list = sorted(text.split())
    max_len = 0
    for item in my_list:
        if len(item) > max_len:
            max_len = len(item)
    for i, item in enumerate(my_list, start=1):
        print(i, item.rjust(max_len))

text_method(text)
