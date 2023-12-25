# ✔Напишите функцию, которая принимает строку текста. ✔Сформируйте список
# с уникальными кодами Unicode каждого символа введённой строки отсортированный
# по убыванию.
#
def chars (text):
    new = []
    for i in set(text):
        new.append(ord(i))
    return sorted(new, reverse=True)

print(chars('age 7iy347f347 c37fc3f83rfcfy3'))
