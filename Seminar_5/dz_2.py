'''Напишите однострочный генератор словаря, который принимает на вход три списка
одинаковой длины: имена str, ставка int, премия str с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве
значения.
Сумма рассчитывается как ставка умноженная на процент премии.
Не забудьте распечатать в конце результат.
Пример использования.
На входе:
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
На выходе:
{'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}'''

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
print({names[0]: salary[0] * float(bonus[0][:-1]) / 100, names[1]:salary[1] * float(bonus[1][:-1]) / 100,
           names[2]: salary[2] * float(bonus[2][:-1]) / 100})

#print({name: (salary_1 * float(bonus_1[:-1])/100) for name, salary_1, bonus_1 in zip(names, salary, bonus)})

#Решение с сайта:

result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)
