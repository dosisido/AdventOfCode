import os
import copy
from functools import cache, wraps
from time import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "file.txt"
N = 1000000000

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = 0
        s = 0
        for _ in range(40):
            time_i = time()
            data = func(*args, **kwargs)
            time_f = time()
            print(f"Tempo di esecuzione: {time_f - time_i}s")
            t += time_f - time_i
            s += 1
        print(f"Tempo medio di esecuzione: {t/s}s")
    return wrapper

def read_file():
    with open(FILE, "r") as f:
        r =  tuple([tuple(x.strip()) for x in f.read().split("\n") if x])
    return r

def collapse_north(table):
    for y in range(1, len(table)):
        for x in range(len(table[y])):
            if table[y][x] == 'O':
                valid = y
                for i in range(y-1, -1, -1):
                    if table[i][x] == '.':
                        valid = i
                    else:
                        break
                if valid != y:
                    table = list(table)
                    table[y] = list(table[y])
                    table[valid] = list(table[valid])
                    table[y][x] = '.'
                    table[valid][x] = 'O'
                    table[y] = tuple(table[y])
                    table[valid] = tuple(table[valid])
                    table = tuple(table)
    return table

def collapse_west(table):
    for x in range(1, len(table[0])):
        for y in range(len(table)):
            if table[y][x] == 'O':
                valid = x
                for i in range(x-1, -1, -1):
                    if table[y][i] == '.':
                        valid = i
                    else:
                        break
                if valid != x:
                    table = list(table)
                    table[y] = list(table[y])
                    table[y][x] = '.'
                    table[y][valid] = 'O'
                    table[y] = tuple(table[y])
                    table = tuple(table)
    return table

def collapse_south(table):
    for y in range(len(table)-2, -1, -1):
        for x in range(len(table[y])):
            if table[y][x] == 'O':
                valid = y
                for i in range(y+1, len(table)):
                    if table[i][x] == '.':
                        valid = i
                    else:
                        break
                if valid != y:
                    table = list(table)
                    table[y] = list(table[y])
                    table[valid] = list(table[valid])
                    table[y][x] = '.'
                    table[valid][x] = 'O'
                    table[y] = tuple(table[y])
                    table[valid] = tuple(table[valid])
                    table = tuple(table)
    return table

def collapse_east(table):
    for x in range(len(table[0])-2, -1, -1):
        for y in range(len(table)):
            if table[y][x] == 'O':
                valid = x
                for i in range(x+1, len(table[y])):
                    if table[y][i] == '.':
                        valid = i
                    else:
                        break
                if valid != x:
                    table = list(table)
                    table[y] = list(table[y])
                    table[y][x] = '.'
                    table[y][valid] = 'O'
                    table[y] = tuple(table[y])
                    table = tuple(table)
    return table

def cicle_print(table):
    t = copy.deepcopy(table)
    table = collapse_north(table)
    table1 = copy.deepcopy(table)
    table = collapse_west(table)
    table2 = copy.deepcopy(table)
    table = collapse_south(table)
    table3 = copy.deepcopy(table)
    table = collapse_east(table)
    table4 = copy.deepcopy(table)
    print_tables(t, table1, table2, table3, table4)
    print("\n\n\n")
    return table

def cicle(table):
    t = copy.deepcopy(table)
    t = collapse_north(t)
    t = collapse_west(t)
    t = collapse_south(t)
    t = collapse_east(t)
    return t

def print_table(table, end = "\n"):
    for y in range(len(table)):
        print(''.join(table[y]))
    print(end=end)

def print_tables(*t):
    if len(t) == 0: return 
    for i in range(len(t[0])):
        for table in t:
            print(''.join(table[i]), end="\t")
        print()

def valuta(table):
    s = 0
    l = len(table)
    for y in range(len(table)):
        for x in range(len(table[y])):
            if table[y][x] == 'O':
                s+= l-y
    return s

def primo():
    table = read_file()
    print_table(table)
    table = collapse_north(table)
    print()
    print_table(table)
    s = valuta(table)
    print(s)

@timing
def secondo():
    table = read_file()
    l = list()
    i = 0
    while i<N:
        table = cicle(table)

        if table in l:
            index = l.index(table)
            delta = len(l) - index
            iter = (N - i) % (delta) -1
            table = l[index + iter]
            break

            # n_ripetizioni = (N - i) // (delta) 
            # i += delta * n_ripetizioni
            # print(index, delta, n_ripetizioni, i)
            # l = []
        else: 
            l.append(copy.deepcopy(table))
        i+=1

    # print_tables(table)
    s = valuta(table)
    print(s)

def main():
    # primo()
    secondo()

if __name__ == "__main__":
    main()