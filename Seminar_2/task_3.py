'''Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.'''

import decimal
import math
decimal.getcontext().prec = 48
pi = decimal.Decimal(str(math.pi))

radius = decimal.Decimal(input('Введите радиус: '))
print(f'Длина окружности = {len(str(2 * radius * pi))}')
print(f'Длина окружности = {2 * radius * pi}')