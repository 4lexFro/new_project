'''На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с
числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей.
Дроби упрощать не нужно.
Для проверки своего кода используйте модуль fractions.
Пример
На входе:
frac1 = "1/2"
frac2 = "1/3"
На выходе:
Сумма дробей: 5/6
Произведение дробей: 1/6
Сумма дробей: 5/6
Произведение дробей: 1/6'''
from fractions import Fraction
def sum_and_product(frac1, frac2):
    # Разделение строк на числитель и знаменатель:
    numer1, denom1 = map(int, frac1.split('/'))
    numer2, denom2 = map(int, frac2.split('/'))
    # Вычисление суммы дробей:
    sum_numer = numer1 * denom2 + numer2 * denom1
    sum_denom = denom1 * denom2
    # Вычисление произведения дробей:
    prod_numer = numer1 * numer2
    prod_denom = denom1 * denom2
    # Возвращение результатов в виде строк:
    return f'{sum_numer}/{sum_denom}', f'{prod_numer}/{prod_denom}'
frac1 = '1/2'
frac2 = '1/3'

sum_frac, prod_frac = sum_and_product(frac1, frac2)
print(f'Сумма дробей: {sum_frac}')
print(f'Произведение дробей: {prod_frac}')

numer1, denom1 = map(int, frac1.split('/')) # Проверка ответа через Fractions
numer2, denom2 = map(int, frac2.split('/'))
print(f'Сумма дробей: {Fraction(numer1, denom1) + Fraction(numer2, denom2)}')
print(f'Произведение дробей: {Fraction(numer1, denom1) * Fraction(numer2, denom2)}')





