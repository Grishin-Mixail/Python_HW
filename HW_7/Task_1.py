# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

import random
import string
import os


def create_group_files (numb: int):
    #создаем необходимое количество файлов с одинаквым расширением

    data = 1
    for _ in range(numb):
        i = random.choice(string.ascii_uppercase)
        file_name = 'file{}.txt'.format(i)
        with open(file_name,'w') as f:
            f.write(str(data))
            data *= 12


def group_rename (new_name: str, exten_old: str, exten_new: str):
    number = 1
    dir_list = os.listdir()
    for obj in dir_list:
        if os.path.isfile(obj) == True and obj[-3:] == exten_old:
            os.rename(obj, '{}_{}.{}'.format(new_name, number,exten_new))
            number += 1
        


create_group_files(4)
group_rename("test","txt","rtf")
