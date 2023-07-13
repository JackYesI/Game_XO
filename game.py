print(' 1 ', "|" , ' 2 ', "|", ' 3 ',sep='') 
print(11 * "-")
print(' 4 ' , "|" , ' 5 ', "|", ' 6 ',sep='')
print(11 * "-")
print(' 7 ' , "|" , ' 8 ', "|", ' 9 ',sep='')

import random

matrix = ['-','-','-','-','-','-','-','-','-']

def checkWin(list, sym):
    if list[0] == list[1] and list[0] == list[2] and list[2] == sym:
        return True
    elif list[3] == list[4] and list[3] == list[5] and list[5] == sym:
        return True
    elif list[6] == list[7] and list[6] == list[8] and list[8] == sym:
        return True
    elif list[0] == list[4] and list[0] == list[8] and list[8] == sym:
        return True
    elif list[2] == list[4] and list[2] == list[6] and list[6] == sym:
        return True
    elif list[0] == list[3] and list[0] == list[6] and list[6] == sym:
        return True
    elif list[1] == list[4] and list[1] == list[7] and list[7] == sym:
        return True
    elif list[2] == list[5] and list[2] == list[8] and list[8] == sym:
        return True
    else:
        return False

def ShowMatrix(list):
    for item in range(9):
            print(list[item], end='')
            if item == 2 or item == 5 or item == 8:
                print('\n')


count = 1

for i in range(0,9):


    if count % 2 == 0:
        step_ = random.randint(0, 8)
        while matrix[step_] != '-':
             step_ = random.randint(0, 8)
        matrix.pop(step_)
        matrix.insert(step_, "O")
        if checkWin(matrix, "O"):
            ShowMatrix(matrix)
            print("You lose")
            break
        ShowMatrix(matrix)
    else:
        step_player = int(input("Enter your number: "))
        while matrix[step_player - 1] != '-':
           step_player = int(input("Enter your number: "))
        matrix.pop(step_player - 1)
        matrix.insert(step_player - 1, "X")
        if checkWin(matrix, "X"):
            ShowMatrix(matrix)
            print("You Win")
            break
    count += 1
