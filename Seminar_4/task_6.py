# ✔Функция получает на вход список чисел и два индекса. ✔Вернуть
# сумму чисел между между переданными индексами. ✔Если индекс выходит
# за пределы списка, сумма считается до конца и/или начала списка.

def summ_between (list, start, finish):
    #start=0 if start<0 else start
    #finish=len(list) if finish>len(list) else finish
    return sum(list[start:finish+1])

print(summ_between([1,2,4,5], -5,7))

