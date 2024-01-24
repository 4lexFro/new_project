# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files.
# Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется
# порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих
# файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы
# с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
# Пример использования.
# На входе:
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
# На выходе:
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc

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
