'''На вход подается словарь со списком вещей для похода в
качестве ключа и их массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его
максимальную грузоподъёмность.

Предметы не должны дублироваться.

Результат должен быть в виде словаря {предмет:вес} с вещами в
рюкзаке и сохранен в переменную backpack.

Достаточно получить один допустимый вариант и сохранить в
переменную backpack. Не выводите backpack на экран.

Пример:
На входе:

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

На выходе, например, один из допустимых вариантов может быть таким:

{'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}'''

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
# list_things = list(items.keys())
# res, temp_list, current_weight = set(), [], 0
#
# for i in range((2 ** len(items))):
#     sample = (list(bin(i)[2:].zfill(len(items))))
#     for n in range(len(sample)):
#         if sample[n] == '1':
#             temp_list.append(list_things[n])
#             current_weight += items[list_things[n]]
#             if current_weight > max_weight:
#                 temp_list.pop()
#                 break
#     res.add(' '.join(temp_list))
#     temp_list, current_weight = [], 0
#
# print('Все варианты комплектации рюкзака:')
# for i in sorted(res):
#     print(i)
sorted_things = dict(sorted(items.items(), key=lambda x: -x[1]))
for k, v in sorted_things.items():
    if v <= max_weight:
        print(k, sep='/n')
    max_weight -= v
