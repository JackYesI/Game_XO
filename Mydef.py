import math
def checkWin(list, sym):
    try:
        index = list.index(sym) + 1
    except:
        return False
    size = math.sqrt(len(list))
    while index != 0:
        try:
            list.index(sym, index + 1) + 1
        except:
            return False
        start_row = int(index // size) * size
        start_col = int(index % size) - 1
        if index % size == 0:
            start_row -= size
            start_col = int(size - 1)

        for i in range(int(start_row), int(start_row + size)):
            if list[i] != sym:
                break
            if i == start_row + size - 1:
                return True
        for i in range(0, int(size)):
            if list[int(start_col)] != sym:
                break
            if i == size - 1:
                return True
            start_col += size

        if (index - 1) % (size + 1) == 0 or (index - 1) % (size + 1) == size + 1:
            j = 0
            for i in range(0, int(size)):
                if list[j] != sym:
                    break
                if i == size - 1:
                    return True
                j += int(size) + 1
        if (index - 1) % (size - 1) == 0 or (index - 1) % (size - 1) == size - 1:
            j = int(size - 1)
            for i in range(0, int(size)):
                if list[j] != sym:
                    break
                if i == size - 1:
                    return True
                j += int(size - 1)
        try:
            index = list.index(sym, index) + 1
        except:
            break
        start_row_n = index // size
        start_col_n = index % size
        while (start_col_n == start_col or start_row_n == start_row) or ((index - 1) % (size + 1) == 0 or (index - 1) % (size + 1) == size + 1) or ((index - 1) % (size - 1) == 0 or (index - 1) % (size - 1) == size - 1):
            try:
                index = list.index(sym, index) + 1
            except:
                break
            start_row_n = index // size
            start_col_n = index % size
    return False

def ShowMatrix(list):
    for item in range(len(list)):
            print(list[item], end='')
            if (item + 1) % math.sqrt(len(list)) == 0:
                if item + 1 == 1:
                    continue
                print('\n')

def brain(list):
    import random
    try:
        index = list.index('O') + 1
    except:
        return 
    size = math.sqrt(len(list))
    while index != 0:
        start_row = int(index // size) * size
        start_col = int(index % size) - 1
        if index % size == 0:
            start_row -= size
            start_col = int(size - 1)
        sc = start_col

        for i in range(int(start_row), int(start_row + size)):
            if list[i] == 'X':
                break
            if i == start_row + size - 1:
                j=int(start_row)
                while j!=int(start_row + size):
                    if list[j] != 'O':
                        list.pop(j)
                        list.insert(j, "O")
                        return
                    j += 1
        for i in range(0, int(size)):
            if list[int(start_col)] == 'X':
                break
            if i == size - 1:
                while sc != int(size):
                    if list[int(sc)] != 'O':
                        list.pop(int(sc))
                        list.insert(int(sc), "O")
                        return 
                    sc += size
            start_col += size
        if (index - 1) % (size + 1) == 0 or (index - 1) % (size + 1) == size + 1: 
            j = 0
            for i in range(0, int(size)):
                if list[j] == 'X':
                    break
                if i == size - 1:
                    j = 0
                    while j!= len(list) - 1:
                        if j != 'O':
                            list.pop((index - 1) + int(size) + 1)
                            list.insert((index - 1) + int(size) + 1, "O")
                            return
                        j += int(size) + 1
                j += int(size) + 1
        if (index - 1) % (size - 1) == 0 or (index - 1) % (size - 1) == size - 1:
            j = int(size - 1)
            for i in range(0, int(size)):
                if list[j] == 'X':
                    break
                if i == size - 1:
                    j = int(size - 1)
                    while j!= len(list) - size - 1:
                        if j != 'O':
                            list.pop((index - 1) + int(size) - 1)
                            list.insert((index - 1) + int(size) - 1, "O")
                            return
                        j += int(size - 1)
                j += int(size - 1)

        try:
            index = list.index('O', index) + 1
        except:
            step_ = random.randint(0, len(list)- 1)
            while list[step_] != '-':
                step_ = random.randint(0, len(list)- 1)
            list.pop(step_)
            list.insert(step_, "O")
            break
        start_row_n = index // size
        start_col_n = index % size
        while (start_col_n == start_col or start_row_n == start_row) or ((index - 1) % (size + 1) == 0 or (index - 1) % (size + 1) == size + 1) or ((index - 1) % (size - 1) == 0 or (index - 1) % (size - 1) == size - 1):
            try:
                index = list.index('O', index) + 1
            except:
                break
            start_row_n = index // size
            start_col_n = index % size
    return 
    
def showMatrixChose(size):
    for item in range((int(size * size))):
            print("|{}|{}".format(item + 1,'\t'), end='')
            if (item + 1) % size == 0:
                if item + 1 == 1:
                    continue
                print('\n', end='')
                # print('-'* int(size) * 3) 