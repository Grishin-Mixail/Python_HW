import queen_check as qc
from eight_queen import search as s

# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

data =['29', '82', '58', '31', '43', '74', '66', '15']
print(qc.check(data))


#Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки. *Выведите все успешные варианты расстановок

#s()

# '27', '82', '58', '31', '43', '74', '66', '15'
# '44', '21', '15', '86', '73', '67', '38', '52'
# '23', '64', '16', '87', '48', '51', '35', '72'
# '41', '17', '72', '25', '68', '84', '33', '56'

