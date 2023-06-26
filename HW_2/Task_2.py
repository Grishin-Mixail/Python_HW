#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import math

def fraction():
    frst: str = input("Введите первую дробь в формате x/y (целые числа):")
    scnd: str = input("Введите вторую дробь в формате x/y (целые числа):")
    action: str = input("Введите маь. операцию (сложение - + или умножение - *):")
    a = frst.split("/")
    b = scnd.split("/")
    if action == "+":
        c:int  = math.lcm(int(a[1]),int(b[1]))
        d:int = int(a[0])*(c/int(a[1]))
        e:int = int(b[0])*(c/int(b[1]))
        print("result = " + str(d+e) + "/" + str(c))
    elif action == "*":
        c: int = int(a[0])*int(b[0])
        d: int = int(a[1])*int(b[1])
        e: int = math.gcd(c,d)
        print("result = " + str(c/e) + "/" + str(d/e))

    else:
        print("Выполняются только операции сложения и умножения!!!")


fraction()


