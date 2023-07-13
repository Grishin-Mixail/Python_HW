# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def File_way(link: str):
    a = link.rfind("/")
    b = link.rfind(".")
    c = (link[0:a+1:],link[a+1:b:],link[len(link)-3::])
    return c

b = "/Users/test/Desktop/code/python/database/123.txt"
print(File_way(b))