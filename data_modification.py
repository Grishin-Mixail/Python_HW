
#Найти строку с нужными данными
def find_data(name):
    filename = "data.txt"
    with open(filename, "r") as data:
        for line in data:
            if str(name) in line:
                line = line[:-2]
                line = line.split(",")
                parameters = ["<id:>", "<Name:>", "<Birthday:>", "<Company:>", "<Town:>", "<Phone:>"]
                data = dict(zip(parameters, line))
                return data


#Удалить строку с нужными данными
def data_delete(name):
    filename = "data.txt"
    with open(filename, "r") as data:
        for line in data:
            if str(name) in line:
                data = line
    f = open(filename,"r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != data:
            f.write(i)
    f.truncate()
    f.close()
    return data
            
#Добавить строку
def data_add(data):
    filename = "data.txt"
    with open(filename, "a") as inp:
        inp.write(str(data) + '\n')
    return(data)
 
#Модифицировать строку
def data_mod(name):
    filename = "data.txt"
    with open(filename, "r") as data:
        for line in data:
            if str(name) in line:
                data = line
                print(data)
                a = line
                data = data.split(",")
                b = int(input("Что хотите изменить? (id = 0; ФИО = 1; ДР = 2; Место работы = 3; Город = 4; Телефон = 5)  "))
                c = input("Введите новые данные: ")
                data[b] = c
                data = " ".join(data)
                data = data.replace(" ", ", ")
                f = open(filename,"r+")
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != data:
                        f.write(i)
                    elif i == a:
                        f.write(data)
                f.truncate()
                f.close()
    return data



