import os
import copy

os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "input.txt"
FILE2 = "input_revisit_2.txt"

table = None
flags = None


def check(x, y):
    global flags
    if x < 0 or y < 0 or x >= len(table) or y >= len(table[0]):
        return False
    
    if flags[x][y]:
        return False
    flags[x][y] = True

    if table[x][y] == ".":
        return False

    if table[x][y].isdigit():
        return check(x+1, y) or check(x, y+1) or check(x-1, y) or check(x, y-1) or check(x+1, y+1) or check(x-1, y-1) or check(x+1, y-1) or check(x-1, y+1)

    return True

def check2(x, y):
    global flags
    if x < 0 or y < 0 or x >= len(table) or y >= len(table[0]):
        return False
    
    if flags[x][y]:
        return False
    flags[x][y] = True

    if table[x][y] != "*":
        return False

    if table[x][y].isdigit():
        return check2(x+1, y) or check2(x, y+1) or check2(x-1, y) or check2(x, y-1) or check2(x+1, y+1) or check2(x-1, y-1) or check2(x+1, y-1) or check2(x-1, y+1)

    return True

def rereplace(string, l):
    for el in l:
        string = string.replace(el, "")
    return string

def replaceNotDigit(string):
    new_string = ""
    for char in string:
        if char.isdigit():
            new_string += char
        else:
            new_string += " "
    return new_string


def print_adiacent(x, y):
    if x-1 >= 0 and y-1 >= 0:
        print(table[x-1][y-1], end="")
    if y-1 >= 0:
        print(table[x-1][y], end="")
    if x+1 < len(table) and y-1 >= 0:
        print(table[x-1][y+1], end="")
        print()
    if x-1 >= 0:
        print(table[x][y-1], end="")
    print(table[x][y], end="")
    if x+1 < len(table):
        print(table[x][y+1], end="")
    print()
    if x-1 >= 0 and y+1 < len(table[0]):
        print(table[x+1][y-1], end="")
    if y+1 < len(table[0]):
        print(table[x+1][y], end="")
    if x+1 < len(table) and y+1 < len(table[0]):
        print(table[x+1][y+1], end="")
    print()

def find_adjacent(x, y):
    arr = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and j >= 0 and i < len(table) and j < len(table[0]):
                if table[i][j].isdigit():
                    arr.append(num_info(i, j))

    print(arr)
    arr2 = []
    cords = set()
    for el in arr:
        c = (el['cord']['x'], el['cord']['y'])
        if c not in cords:
            arr2.append(el)
            cords.add(c)

    print(arr2)
    if len(arr2) <2:
        return 0
    if len(arr2) > 2:
        print("error")
        print(arr)
        exit()
    
    return arr2[0]['value'] * arr2[1]['value']

def num_info(x, y):
    string = ""
    i = x
    j = y
    while table[x][j].isdigit() and j>-1:
        j-= 1
    j+= 1
    start = j
    while j<len(table[0]) and table[x][j].isdigit():
        string += table[x][j]
        j+= 1
    
    return {"cord": {'x':x, 'y':start}, 'value': int(string)}

def readTable(file):
    global table
    global flags
    table = []
    flags = []
    with open(file, "r") as f:
        for line in f:
            row = []
            row2 = []
            for char in line.strip():
                row.append(char)
                row2.append(False)
            table.append(row)
            flags.append(row2)

def first():
    global table
    global flags    
    
    flagsCopy = copy.deepcopy(flags)

    for x in range(len(table)):
        print("row: ", x)
        for y in range(len(table[0])):
            if not check(x, y):
                table[x][y] = "."
            flags = copy.deepcopy(flagsCopy)
                
    for row in table:
        print("".join(row))
    print()

    sum = 0
    for row in table:
        string = "".join(row)
        # string = rereplace(string, [".", "#", '*', "$", '+'])
        string = replaceNotDigit(string)
        string = string.strip().split(" ")
        for el in string:
            if el.isdigit():
                # print(el)
                sum += int(el)

    print(sum)

def second():

    sum = 0
    total = 0

    for x in range(len(table)):
        for y in range(len(table[0])):
            if table[x][y] == "*":
                print_adiacent(x, y)
                val = find_adjacent(x, y)
                print(val)
                sum += val
                total += 1
                print()
    print(sum)
    print("Total summed element", total)


def main():
    # first()
    second()


readTable(FILE)

if __name__ == "__main__":
    main()