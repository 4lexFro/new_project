'''2) Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если это число натуральное и делится
нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. Если подается отрицательное
число или число более ста тысяч, выведите на экран сообщение: "Число должно быть больше 1 и меньше
100000".
Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.
Пример
На входе:
num = 2
На выходе:
Простое
На входе:
num = 1000001
На выходе:
Не является простым'''

num = 11
if num <= 0 or num == 1 or num > 100000:
    print('Число должно быть больше 1 и меньше 100000')
    exit(0)
count = 0
for i in range(2, num // 2 + 1):
    if (num % i == 0):
        count += 1
if (count <= 0):
    print('Простое')
else:
    print('Не является простым')
