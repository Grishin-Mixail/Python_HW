from eight_queen import create_field_matrix as cfm

def check(data: list):
    matrix = cfm(8)
    for i in data:
        if int(i[0]) > 8 or int(i[0]) < 0 and int(i[1]) < 0 or int(i[1]) > 8 :
            print("Wrong data!")
            a = 0
        elif matrix[int(i[0])-1][int(i[1])-1] != 1:
            line = int(i[0])-1
            row = int(i[1])-1
            a = line
            b = row
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
        else:
            return False
    if a != 0:
        return True
