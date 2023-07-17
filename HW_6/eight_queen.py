import random
import functools


def printMatrix ( matrix ):
   #aккуратное представление матрицы
    
   for row in matrix: 
      for x in row: 
          print ( "{:4d}".format(x), end = "" ) 
      print ()


def create_field_matrix(n: int):
    #создание матрицы, состоящей из нулей, заданного размера

    matrix = [[] for i in range(n)]
    for i in range(n):
        matrix[i] = [0 for i in range(1, n+1)]
    return matrix

def search():
    matrix = create_field_matrix(8)
    count = 0
    result = 0
    postions =[] 
    while result != 64:
        line = random.randint(0,7)
        row = random.randint(0,7)
        a = line
        b = row
        if matrix[line][row] != 1:
            postions.append(str(line+1)+str(row+1))
            count += 1
            matrix[line][row] = 1

            # заполнение единицами выбранной строки столбца
            for i in range(0,8):
                matrix[line][i] = 1
                matrix[i][row] = 1

            # заполнение диагоналей единицами
            while line != 7 and row != 0:
                line += 1
                row -= 1
                matrix[line][row] = 1
            line = a
            row = b
            while line != 0 and row != 7:
                line -= 1
                row += 1
                matrix[line][row] = 1
            line = a
            row = b
            while line != 0 and row != 0:
                line -= 1
                row -= 1
                matrix[line][row] = 1
            line = a
            row = b
            while line != 7 and row != 7:
                line += 1
                row += 1
                matrix[line][row] = 1
            result = functools.reduce(lambda a,x: a + sum(x), matrix, 0)
    if count == 8:
        print(count,"\n" ,postions)
        printMatrix(matrix)
    else:
        print(count,"\n" ,postions)

search()