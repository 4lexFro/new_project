'''Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.'''

'''gen_odd = (i for i in range(1, 100) if (i % 3 == 0 ,print('Fizz')))
print(*gen_odd)
'''

'''for i in range(1, 20):
    result = ''
    # if i % 3 == 0 and i % 5 == 0:
    #    result += 'FizzBuzz'

    if i % 3 == 0:
        result += 'Fizz'
    if i % 5 == 0:
        result += 'Buzz'
    print(i if result == '' else result)'''

output = ('FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 101))
print(*output)
