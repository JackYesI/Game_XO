import Mydef
import random
import math

matrix = []
size_matrix = 0

while size_matrix < 3:
    size_matrix = int(input("Enter area from three: "))

size_matrix = size_matrix * size_matrix
for i in range(size_matrix):
    matrix.append('-')


count = 1

for i in range(size_matrix):


    if count % 2 == 0:
        step_ = random.randint(0, len(matrix)- 1)
        while matrix[step_] != '-':
             step_ = random.randint(0, len(matrix)- 1)
        matrix.pop(step_)
        matrix.insert(step_, "O")
        if Mydef.checkWin(matrix, "O"):
            Mydef.ShowMatrix(matrix)
            print("You lose")
            break
        Mydef.ShowMatrix(matrix)
    else:
        step_player = int(input("Enter your number: "))
        while matrix[step_player - 1] != '-':
           step_player = int(input("Enter your number: "))
        matrix.pop(step_player - 1)
        matrix.insert(step_player - 1, "X")
        if Mydef.checkWin(matrix, "X"):
            Mydef.ShowMatrix(matrix)
            print("You Win")
            break
    count += 1
