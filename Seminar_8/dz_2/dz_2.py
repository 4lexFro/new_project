# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
#
# Создайте файл __init__.py и запишите в него все функции:
# get_dir_size,
# save_results_to_json,
# save_results_to_csv,
# save_results_to_pickle, traverse_directory

my_code_to_write_8_1 = '''
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
    return size*count

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
'''

with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write(my_code_to_write_8_1)
