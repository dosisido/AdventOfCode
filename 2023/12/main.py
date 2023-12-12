import os
from functools import cache
from typing import List, Tuple
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "file.txt"
PRINT = False

def read_file():
    with open(FILE, "r") as f:
        for line in f:
            l = line.strip().split()
            c = l[0].count("?")
            l[0] = [i for i in l[0]]
            l[1] = tuple([int(x) for x in l[1].split(",")])
            l.append(c)
            yield l

def isValid(line, occurrences):
    s = "".join(line).split(".")
    i = 0
    for e in s:
        if len(e) == 0: continue
        if i >= len(occurrences): return False
        if len(e) != occurrences[i]: return False
        i += 1
    if i != len(occurrences): return False
    return True

def isValidBackwards(line, occurrences):
    s = "".join(line[::-1]).split(".")
    i = len(occurrences)-1
    for e in reversed(s):
        if len(e) == 0: continue
        if i < 0: return False
        if len(e) != occurrences[i]: return False
        i -= 1
    if i != -1: return False
    return True


def stampa(line, i):
    print('\033[F', end='')
    print('\033[F', end='')
    print(" "*i, 'v', sep='')
    print("".join(line))

def rico(line, occurrences, i, n):
    if n==0:
        return 1 if isValid(line, occurrences) else 0
    if i == len(line): return 0
    if line[i] != '?': return rico(line, occurrences, i+1, n)
    if PRINT: stampa(line, i)

    line[i] = '.'
    r = rico(line, occurrences, i+1, n-1)
    line[i] = '#'
    r+= rico(line, occurrences, i+1, n-1)
    line[i] = '?'
    return r

def rico_ricombinazione(subline, occurrences):
    if len(subline) == 0:
        # se è finita la stringa e non ci sono più occorrenze da controllare
        if len(occurrences) == 0: return 1
        # se è finita la stringa ma ci sono ancora occorrenze da controllare
        return 0
    
# presa da internet!!!
@cache
def count_valid_cached(springs: str, groups: Tuple[int]):
    if len(springs) == 0:
        if len(groups) == 0:
            return 1
        else:
            return 0

    curr = springs[0]
    if curr == "#":
        if len(groups) == 0 or len(springs) < groups[0]:
            return 0

        if "." in springs[0 : groups[0]]:
            return 0

        if springs[groups[0] :].startswith("#"):
            return 0

        if len(springs) > groups[0]:
            if springs[groups[0]] == "?":
                return count_valid_cached(springs[groups[0] + 1 :].lstrip("."), groups[1:])

        return count_valid_cached(springs[groups[0] :].lstrip("."), groups[1:])
    elif curr == ".":
        return count_valid_cached(springs.lstrip("."), groups)
    elif curr == "?":
        return count_valid_cached("#" + springs[1:], groups) + count_valid_cached("." + springs[1:], groups)

# to_do
def rico_pure_function(sublist: str, groups: Tuple[int]):
    if len(sublist) == 0:
        if len(groups) == 0 : return 1
        return 0
    if len(groups) == 0: return 0

    char = sublist[0]
    sublist = sublist[1:]

    if char == '#':
        if groups[0] > 0:
            groups[0]-= 1
            return rico_pure_function(sublist, groups)

        else: return 0
    elif char == '.':
        if groups[0]: pass


def primo():
    s = 0
    i = 1
    for char, occurrences, n in read_file():
        print(char, occurrences, n)
        r = rico(char, occurrences, 0, n)
        print(f"Line {i:3}: {r}")
        s+= r
        i+=1
        
    print("Total:", s)

def secondo():
    s = 0
    i = 1
    for char, occurrences, n in read_file():
        print(char, occurrences, n)
        char.append('?')
        char = char * 5
        char.pop()
        occurrences = occurrences * 5
        n = n*5 + 4
        
        if PRINT: print(''.join(char))
        if PRINT: print("\n\n", end='')
        r = count_valid_cached("".join(char), occurrences)
        if PRINT:
            print('\033[F', end='')
            print('\033[F', end='')
        print(f"Line {i:3}: {r}")
        s+= r
        i+=1
        
    print("Total:", s)

def main():
    # primo()
    secondo()

if __name__ == "__main__":
    main()