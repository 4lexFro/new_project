# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# Создайте файл __init__.py и запишите в него функцию rename_files

my_code_from_file = '''
import os


def rename_files(old_name_diapason: list = None, desired_name: str = 'new_file', num_digits: int = 3,
                 source_ext: str = 'txt', target_ext: str = 'new'):
    count = 0
    for file in os.listdir('test_folder'):
        name, extension = os.path.splitext(file)

        if extension[1:] == source_ext:
            count += 1
            out_name = ''
            if old_name_diapason:
                out_name += ''.join(name[old_name_diapason[0] - 1:old_name_diapason[1]])
            out_name += desired_name + f'{count:0{num_digits}}' + '.' + target_ext
            os.rename('test_folder/'+file, 'test_folder/'+out_name)
'''

with open('__init__.py', 'a', encoding='utf-8') as f:
    for line in my_code_from_file:
        f.write(line)