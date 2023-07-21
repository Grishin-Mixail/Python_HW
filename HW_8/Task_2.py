# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
# Распечатайте его как pickle строку.

import csv
import pickle

def csv_to_pickles():

    with (
        open('dict.csv', 'r', newline='') as f_read,
        open('String.pickle', 'wb') as f_write
    ):
        all_data = ""
        csv_file = csv.reader(f_read)
        for i, line in enumerate(csv_file):
            if i != 0:
                for data in line:
                    all_data = all_data + data


        res = pickle.dumps(all_data, protocol=pickle.DEFAULT_PROTOCOL)
        pickle.dump(res, f_write)


csv_to_pickles()