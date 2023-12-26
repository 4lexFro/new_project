# В большой текстовой строке text подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр
# символов.
#
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
#
# Отсортируйте по убыванию значения количества повторяющихся слов.
#
# Пример
#
# На входе:
#
text = 'Hello world. Hello Python. Hello again.'
#
# На выходе:
#
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

from collections import Counter
import string
import re
low_text = (re.sub(r'[^\w\s]', ' ', text)).lower()
my_list = (''.join([i for i in low_text if not i.isdigit()])).split()
Counters_found = Counter(my_list)
most_occur = Counters_found.most_common(10)
print(most_occur)