# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

with open('names.txt', 'r', encoding='UTF-8') as file_names:
    # print([row.strip() for row in file.readlines()]) # Readlines считывает все строки из файла и удаляет
    # '\n' в конце всех имен
    # print(file.read().split('\n')) # Read выводит все имена в одну строку, в конце каждого
    # имени будет '\n' и split будет их вырезать. Результат и в первом, и во втором случае одинаковый -
    # - список строчных имен

    names = [row.strip() for row in file_names.readlines()]
with open('nums.txt', 'r', encoding='UTF-8') as file_nums:
    nums = [row.strip() for row in file_nums.readlines()]

numbers = []
for row in nums:
    first, second = row.split(' | ')
    numbers.append((int(first), float(second)))

result = []
for i in range(len(max([names, numbers], key=len))):
    number = numbers[i][0] * numbers[i][1]
    result.append((names[i].upper(), round(number)) if number > 0 else (names[i].lower(), abs(number)))
with open('result.txt', 'w', encoding='UTF-8') as result_file:
    result_file.write('\n'.join([f'{row[0]} | {row[1]}' for row in result]))
for row in result:
    print(row)
