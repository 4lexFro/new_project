# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и
# все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
# Каждый результат должен содержать следующую информацию:
#
# Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория.
# Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
# Важные детали:
#
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
#
# Для файлов сохраните их размер в байтах.
#
# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории,
# и вложенных директорий.
#
# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
#
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
#
# Для обхода файловой системы вы можете использовать модуль os.
#
# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и возвращать
# результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных файлах
# (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
#
# Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий.
# При этом сначала добавляются файлы, а затем директории.
#
# Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)),
# и затем получается размер файла (size = os.path.getsize(path)). Информация о файле добавляется в список results
# в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.
#
# Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)),
# и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого.
# Информация о директории добавляется в список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.

import csv
import json
import os
import pickle


def get_dir_size(path):
    size = 0
    count = 1
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            size += os.path.getsize(item_path)
        else:
            count += 1
            size += get_dir_size(item_path)
    return size * count


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for dir_ in dirs:
            path = os.path.join(root, dir_)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results


def save_results_to_json(results, output: str = 'results.json'):
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)


def save_results_to_csv(results, output: str = 'results.csv'):
    if results:
        with open(output, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)


def save_results_to_pickle(results, output: str = 'results.pkl'):
    with open(output, 'wb') as f:
        pickle.dump(results, f)
