#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
#Функцию hex используйте для проверки своего результата.

import math

def MyHex(num):
    hex = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, \
           10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f",}
    res: list = []
    while num % 16 > 0:
        res.insert(0,hex[num % 16])
        num = num // 16
    for i in res:
        print(i, end = "")
    print()

MyHex(2222)
print(hex(2222))