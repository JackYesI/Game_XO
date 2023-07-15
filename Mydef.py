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
            index = list.index(sym, index + 1) + 1
        except:
            break
        start_row_n = index // size
        start_col_n = index % size
        while (start_col_n == start_col or start_row_n == start_row) or ((index - 1) % (size + 1) == 0 or (index - 1) % (size + 1) == size + 1) or ((index - 1) % (size - 1) == 0 or (index - 1) % (size - 1) == size - 1):
            try:
                index = list.index(sym, index + 1) + 1
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
    