import csv
with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
    print(type(line))

# Функция csv.reader принимает на вход файловый дескриптор и построчно читает информацию.
# Важно! При работе с CSV необходимо указывать параметр newline=’’ во время открытия файла.