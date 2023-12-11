import os
from collections import deque
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = 'file.txt'
EXPAND_COEFFICIENT = 1000000


class Tile:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        

    def __str__(self) -> str:
        return f'{self.x:3}-{self.y:3}'
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Tile):
            return self.x == o.x and self.y == o.y
        return False
    


def read_file():
    t = []
    with open(FILE, 'r') as f:
        for line in f:
            t.append([x for x in line.strip()])    
    return t

def expand_universe(table):
    table2 = []
    for i in range(len(table)):
        row = []
        check = False
        for j in range(len(table[i])):
            row.append(table[i][j])
            if table[i][j] == '#':
                check = True
        if not check:
            table2.append(list(row))
        table2.append(row)

    table = table2
    table2 = [[] for _ in range(len(table))]

    for i in range(len(table[0])):
        check = False
        for j in range(len(table)):
            table2[j].append(table[j][i])
            if table[j][i] == '#':
                check = True
        if not check:
            for j in range(len(table)):
                table2[j].append('.')
            

    return table2

def expand_universe2(table):

    expand_rows = []
    expand_cols = []

    for i in range(len(table)):
        check = False
        for j in range(len(table[i])):
            if table[i][j] == '#':
                check = True
        if not check:
            expand_rows.append(i)


    for i in range(len(table[0])):
        check = False
        for j in range(len(table)):
            if table[j][i] == '#':
                check = True
        if not check:
            expand_cols.append(i)            

    return expand_cols, expand_rows

def at_tile(tiles, t:Tile):
    return tiles[t.x][t.y]

def dfs(tiles, start, toVisit):
    stack = deque()
    toVisit = set(toVisit)
    stack.append((start, 0))
    visited = set()
    r = {}

    while stack and len(toVisit) > 0:
        current = stack.popleft()
        if current[0] in visited:
            continue
        visited.add(current[0])

        if current[0].x < 0 or current[0].x >= len(tiles[0]) or current[0].y < 0 or current[0].y >= len(tiles):
            continue

        # print(current[0], current[1])

        if current[0] in toVisit:
            r[current[0]] = current[1]
            toVisit.remove(current[0])
        
        stack.append((Tile(current[0].x-1, current[0].y), current[1]+1))
        stack.append((Tile(current[0].x+1, current[0].y), current[1]+1))
        stack.append((Tile(current[0].x, current[0].y-1), current[1]+1))
        stack.append((Tile(current[0].x, current[0].y+1), current[1]+1))


    return r

def dfs2(tiles, start, toVisit, expand_cols, expand_rows):
    stack = deque()
    toVisit = set(toVisit)
    stack.append((start, 0))
    visited = set()
    r = {}

    while stack and len(toVisit) > 0:
        current = stack.popleft()
        if current[0].x < 0 or current[0].x >= len(tiles[0]) or current[0].y < 0 or current[0].y >= len(tiles):
            continue
        if current[0] in visited:
            continue
        visited.add(current[0])


        # print(f"{current[0]}  d:{current[1]}")

        if current[0] in toVisit:
            r[current[0]] = current[1]
            toVisit.remove(current[0])
        
        dist = current[1] + EXPAND_COEFFICIENT if current[0].x-1 in expand_cols else current[1] + 1
        stack.append((Tile(current[0].x-1, current[0].y), dist))

        dist = current[1] + EXPAND_COEFFICIENT if current[0].x+1 in expand_cols else current[1] + 1
        stack.append((Tile(current[0].x+1, current[0].y), dist))
        
        dist = current[1] + EXPAND_COEFFICIENT if current[0].y-1 in expand_rows else current[1] + 1
        stack.append((Tile(current[0].x, current[0].y-1), dist))
        
        dist = current[1] + EXPAND_COEFFICIENT if current[0].y+1 in expand_rows else current[1] + 1
        stack.append((Tile(current[0].x, current[0].y+1), dist))


    return r

def stars_and_pairs(table):
    stars = []
    pairs = {}

    for y in range(len(table)):
        for x in range(len(table[y])):
            if table[y][x] == '#':
                stars.append(Tile(x, y))

    for y in range(len(stars)):
        r  = []
        for x in range(y+1, len(stars)):
            r.append(stars[x])
        pairs[stars[y]] = r

    return stars, pairs

def print_pairs(pairs):
    print("Pairs:")
    s=0
    for key, value in pairs.items():
        s+=len(value)
        print(f"{key}, ({len(value)})", end=': ')
        for e in value:
            print(f"({e})", end=' ')
        print()
    print(s)

def primo(prnt = False):
    table = read_file()
    table = expand_universe(table)
    stars, pairs = stars_and_pairs(table)


    if False: print_pairs(pairs)

    s = 0
    for key, value in pairs.items():
        r = dfs(table, key, value) 
        print(f"From {key} ({stars.index(key)+1}):")
        for k, v in r.items():
            if prnt: print(f"{k} ({stars.index(key)+1}), {v}")
            s+=v
        if prnt: print()

    print(s)

def secondo(prnt = False):
    table = read_file()
    expand_cols, expand_rows = expand_universe2(table)
    print(expand_cols, expand_rows)
    stars, pairs = stars_and_pairs(table)

    s = 0
    for key, value in pairs.items():
        r = dfs2(table, key, value, expand_cols, expand_rows)
        print(f"From {key} ({stars.index(key)+1}):")
        for k, v in r.items():
            if prnt: print(f"{k} ({stars.index(key)+1}), {v}")
            s+=v
        if prnt: print()

    print(s)

def both():
    original = read_file()
    table_exp = expand_universe(original)
    expand_cols, expand_rows = expand_universe2(original)
    print(expand_cols, expand_rows)
    stars_expanded, pairs_expanded = stars_and_pairs(table_exp)
    stars_original, pairs_original = stars_and_pairs(original)

    s = 0
    for i in range(len(pairs_expanded)):
        key_expanded = list(pairs_expanded.keys())[i]
        key_original = list(pairs_original.keys())[i]
        value_expanded = pairs_expanded[key_expanded]
        value_original = pairs_original[key_original]
        
        r_expanded = dfs(table_exp, key_expanded, value_expanded)
        r_original = dfs2(original, key_original, value_original, expand_cols, expand_rows)
        print(f"From {key_expanded} ({stars_expanded.index(key_expanded)+1}): {len(r_expanded)}")
        print(f"From {key_expanded} ({stars_expanded.index(key_expanded)+1}): {len(r_original)}")
        if len(r_expanded) != len(r_original):
            print("ERROR")
            exit(1)
        
        for j in range(len(r_expanded)):
            k_expanded = list(r_expanded.keys())[j]
            k_original = list(r_original.keys())[j]
            v_expanded = r_expanded[k_expanded]
            v_original = r_original[k_original]
            print(f"\t{k_expanded} ({stars_expanded.index(k_expanded)+1}), {v_expanded}")
            print(f"\t{k_original} ({stars_original.index(k_original)+1}), {v_original}")
            if v_expanded != v_original:
                print("ERROR")
                exit(1)
            print("-----")

        # for k, v in r.items():
        #     if prnt: print(f"{k} ({stars.index(key)+1}), {v}")
        #     s+=v
        # if prnt: print()



def main():
    # primo()
    secondo()

    # both()

    
if __name__ == "__main__":
    main()