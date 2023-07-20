# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


import math
import csv
import random
import json



def main(func):   
    def wrapper(a,b,c):
        data = []
        with open('data.csv', 'r', newline='') as f:
            csv_file = csv.reader(f)
            for i, line in enumerate(csv_file):
                if i != 0:
                    a,b,c = line
                    result = func(float(a),float(b),float(c))
                    if result != None:
                        data.append({"a" : a, "b" : b, "c" : c, "result" : result})
                    with open('new_user.json', 'w') as f:
                        json.dump(data, f)
        return result
    return wrapper

@main
def square_root_eq(a, b, c):
    discr = b ** 2 - 4 * a * c    
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        return x
    else:
        return "Roots are not exist!!!"

def csv_creater():
    with open("data.csv", "w", encoding='utf-8',newline='') as w_file:
        names = ["one", "two", "three"]
        file_writer = csv.DictWriter(w_file, delimiter = ",",
                                    dialect='excel', fieldnames=names)
        file_writer.writeheader()
        for _ in range(10):
            one = random.randint(-100, 100)
            two = random.randint(-100, 100)
            three = random.randint(-100, 100)
            file_writer.writerow({"one": one, "two": two, "three": three})

csv_creater() 
square_root_eq(0,0,0)


        
