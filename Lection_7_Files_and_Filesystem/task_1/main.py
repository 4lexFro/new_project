# f = open('data_text.txt', 'r', encoding='utf-8')
# print(f)
# print(list(f))

# f = open('data_text.txt', 'a', encoding='utf-8')
# f.write('Окончание файла\n')
# f.close()

#Менеджер контекста with open
with open('data_text.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
print(f.write('Пока,пока!'))