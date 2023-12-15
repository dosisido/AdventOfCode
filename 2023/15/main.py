import os
from functools import cache
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = 'file.txt'

@cache
def H(old: int, char: str) -> int:
    return ((old + ord(char))* 17) % 256

def H_wrapper(s:str) -> int:
    h = 0
    for c in s:
        if c == '-' or c == '=':
            return h, s[-1] if c == '=' else None
        h = H(h, c)

def read_file() -> str:
    with open(FILE, 'r') as f:
        for x in f.read().split(','):
            yield x

def primo():
    s = 0
    for x in read_file():
        h = 0
        for c in x:
            h = H(h, c)
        s += h
    print(s)

def find_index(l, el):
    for index in range(len(l)):
        if l[index][0] == el:
            return index
    return -1 

def stampa(l):
    for index in range(len(l)):
        if len(l[index]) == 0: continue
        print(f'{index}: {l[index]}')

def secondo(prnt = False):

    l = []
    for _ in range(256): l.append([])

    for el in read_file():
        if prnt: print(el)
        index, last = H_wrapper(el)
        if last:    # =
            label = el.split('=')[0]
            find = find_index(l[index], label)
            if find == -1:
                l[index].append((label, int(last)))
            else:
                l[index][find] = (label, int(last))
        else:
            label = el.split('-')[0]
            find = find_index(l[index], label)
            if find != -1:
                l[index].pop(find)
        
        if prnt: stampa(l[0:4])
        if prnt: print()
    
    s = 0
    for line_index in range(len(l)):
        line = l[line_index]
        for el_index in range(len(line)):
            el = line[el_index]
            s+= (line_index+1) * (el_index+1) * el[1]
    print(s)



def main():
    secondo()

if __name__ == "__main__":
    main()