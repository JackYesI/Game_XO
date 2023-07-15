import Mydef
import random
import math

print("for matrix 3*3")
print(' 1 ', "|" , ' 2 ', "|", ' 3 ',sep='') 
print(11 * "-")
print(' 4 ' , "|" , ' 5 ', "|", ' 6 ',sep='')
print(11 * "-")
print(' 7 ' , "|" , ' 8 ', "|", ' 9 ',sep='')

matrix = []
size_matrix = 0

while size_matrix < 3:
    size_matrix = int(input("Enter area from three: "))


size_matrix = size_matrix * size_matrix
for i in range(size_matrix):
    matrix.append('-')

z = 0
count = 1

for i in range(size_matrix):

    if count % 2 == 0:
        if z == 1:
            z += 1
            count += 1
            continue
        Mydef.brain(matrix)
        if Mydef.checkWin(matrix, "O"):
            Mydef.ShowMatrix(matrix)
            print("You lose")
            break
        Mydef.ShowMatrix(matrix)
    else:
        Mydef.showMatrixChose(math.sqrt(size_matrix))
        step_player = int(input("Enter your number: "))
        while matrix[step_player - 1] != '-':
           step_player = int(input("Enter your number: "))
        matrix.pop(step_player - 1)
        matrix.insert(step_player - 1, "X")
        if z == 0:
            step_ = random.randint(0, len(matrix)- 1)
            while matrix[step_] != '-':
                step_ = random.randint(0, len(matrix)- 1)
            matrix.pop(step_)
            matrix.insert(step_, "O")
            z += 1
            Mydef.ShowMatrix(matrix)
        if Mydef.checkWin(matrix, "X"):
            Mydef.ShowMatrix(matrix)
            print("You Win")
            break
    count += 1
    if i == size_matrix - 1:
        print('draw')

