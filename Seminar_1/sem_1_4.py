'''Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
📌Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********'''
space = " "
star = "*"
tree = int(input('Сколько рядов у елки?: '))
spaces = tree - 1
stars = 1
for i in range(tree):
    print((space * spaces) + (star * stars))
    stars += 2
    spaces += 1
