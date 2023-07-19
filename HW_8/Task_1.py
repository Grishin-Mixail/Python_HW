# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
# Для тестированию возьмите pickle версию файла из предыдущей задачи. 
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle

def pickle_to_csv():

    with (
        open('dict.pickle', 'rb') as f_read,
        open('dict.csv', 'w', encoding='utf-8') as f_write
    ):
        read = pickle.load(f_read)
        a = []
        for i in read:          
            for k,v in i.values():
                a.append({"father": k, "mother": v})     

        write = csv.DictWriter(f_write, fieldnames=["father", "mother"])
        write.writeheader()
        write.writerows(a)
        


pickle_to_csv()