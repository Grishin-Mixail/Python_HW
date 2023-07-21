#  Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию. 
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий 
# размер файлов в ней с учётом всех вложенных файлов и директорий. 


import os
import json
import csv
import pickle


def write_json_csv_pickle(directory):
    with (
            open('dir.json', 'w', encoding='utf-8') as j_file,
            open('dir.csv', 'w', encoding='utf-8') as c_file,
            open('dir.pickle', 'wb') as p_file
    ):
        #JSON
        result_dict_json = {}
        for dir_path, dir_name, file_name in os.walk(directory):
            result_dict_json[f'Directory - {dir_path} = {os.path.getsize(dir_path)} byte'] = [
                f'File - {i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in file_name]
        json.dump(result_dict_json, j_file, indent=4, separators=(',', ':'))

        #CSV
        data = [["Dir", "Files"]]
        for key, value in result_dict_json.items():
            data.append([key, value])
        write_csv = csv.writer(c_file, dialect='excel-tab', delimiter=',')
        write_csv.writerows(data)

        #PICKLE
        pickle.dump(result_dict_json, p_file)


write_json_csv_pickle(os.getcwd())

