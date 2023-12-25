# Функция принимает на вход три списка одинаковой длины: ✔
# имена str, ✔ ставка int, ✔ премия str с указанием процентов
# вида «10.25%». ✔Вернуть словарь с именем в качестве ключа и
# суммой премии в качестве значения. ✔Сумма рассчитывается как
# ставка умноженная на процент премии.
# def bonus_calculation(names, base, bonus):
#     result = {}
#     for i in range(len(base)):
#         result[names[i]] = (base[i] * float(bonus[i][:-1])/100)
#
#     return result
#
# print(bonus_calculation(["ivan", "maxim"], [3000,4500], ["0.25%", "0.33%"]))

def solution(names, salary, bonus):
    data = list(zip(names, salary, bonus))
    return {item[0]: item[1]*float(item[2].replace('%', ''))/100 for item in data}


print(solution(["ivan", "maxim"], [3000, 4500], ["0.25%", "0.33"]))