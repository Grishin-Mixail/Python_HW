#Задача1: Таблица умножения:

# start = 2
# end = 10
# list_1 = range(start,end+1,1)
# list_2 = range(start,end-4,1)
# result_1 = ""
# result_2 = ""
# for row in list_1:
#     for col in list_2:
#         if row == 10:
#             result_1 = result_1 + str(str(col) + " x " + str(row) + " =" + str(col*row) + "     ")
#         elif row < 10 and col*row>=10:
#             result_1 = result_1 + str(str(col) + " x " + str(row) + " = " + str(col*row) + "     ")
#         else:
#             result_1 = result_1 + str(str(row) + " x " + str(col) + " =  " + str(col*row) + "     ")

#     print(result_1)
#     result_1 = ""
# print()
# list_2 = range(start+4,end,1)
# for row in list_1:
#     for col in list_2:
#         if row == 10:
#             result_1 = result_1 + str(str(col) + " x " + str(row) + " =" + str(col*row) + "     ")
#         elif row < 10 and col*row>=10:
#             result_1 = result_1 + str(str(col) + " x " + str(row) + " = " + str(col*row) + "     ")
#         else:
#             result_1 = result_1 + str(str(row) + " x " + str(col) + " =  " + str(col*row) + "     ")

#     print(result_1)
#     result_1 = ""

#Задача2: Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с 
# суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника 
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

# a = input("1st side lenght: ")
# b = input("2nd side lenght: ")
# c = input("3rd side lenght: ")

# if a==b==c:
#     print("Равносторонний")
# elif ((a+b)<c and (a+c)>b and (c+b)>a) or ((a+b)>c and (a+c)<b and (c+b)>a) or ((a+b)>c and (a+c)>b and (c+b)<a):
#     if a==b or a==c or b==c:
#         print("Равнобедренный")
#     else:
#         print("Разносторонний")
# else:
#     print("Треугольник не существует!")

#Задача3: Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. С
# делайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
# import math
# a = int(input("Введите число: "))

# for i in range(2,int(math.sqrt(a))+1):
#     if (a%i) == 0:
#       print("Число составное")
#       break
#     else:
#         print("Число простое")
#         break

    
#Задача4: Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки.

# from random import randint

# num = randint(0, 1001)
# count = 0

# while True:
#     a = int(input("Введите число: "))
#     if count != 10:        
#         if num>a:
#             print("больше")
#         elif num<a:
#             print("меньше")
#         else:
#             print("угадал:)")
#             break
#         count += 1
#     else:
#         print("Попытки кончились!")
#         break
        


