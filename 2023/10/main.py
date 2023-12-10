import os
from collections import deque
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "file.txt"
SAVE_FILE = "save.txt"

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.x == other.x and self.y == other.y
        return False
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __str__(self):
        return f"Tile({self.x}, {self.y})"
    

def read_file():
    table = []
    with open(FILE, "r") as f:
        for line in f.readlines():
            table.append(list(line.strip()))
    return table

def enlarge_table(table):
    table2 = []
    for y in range(len(table)):
        row = []
        for x in range(len(table[y])):
            row.append(table[y][x])
            row.append("-")
        table2.append(row)
        row = ['|' for _ in range(len(row))]
        table2.append(row)
    return table2
        
def reduce_table(table):
    table2 = []
    for y in range(len(table)):
        if y % 2 == 1:
            continue
        row = []
        for x in range(len(table[y])):
            if x % 2 == 1:
                continue
            row.append(table[y][x])
        table2.append(row)
    return table2

def save_file(table):
    with open(SAVE_FILE, "w") as f:
        for row in table:
            f.write("".join(row))
            f.write("\n")

def starting_tile(table):
    for y in range(len(table)):
        for x in range(len(table[y])):
            if table[y][x] == "S":
                return Tile(x, y)

def neighbors_per_follow(table, tile :Tile):   
    if table[tile.y][tile.x] == "|":
        return (Tile(tile.x, tile.y+1), Tile(tile.x, tile.y-1))
    elif table[tile.y][tile.x] == "-":
        return (Tile(tile.x+1, tile.y), Tile(tile.x-1, tile.y))
    elif table[tile.y][tile.x] == "L":
        return (Tile(tile.x+1, tile.y), Tile(tile.x, tile.y-1))
    elif table[tile.y][tile.x] == "J":
        return (Tile(tile.x-1, tile.y), Tile(tile.x, tile.y-1))
    elif table[tile.y][tile.x] == "7":
        return (Tile(tile.x-1, tile.y), Tile(tile.x, tile.y+1))
    elif table[tile.y][tile.x] == "F":
        return (Tile(tile.x+1, tile.y), Tile(tile.x, tile.y+1))
    return []

def around_start(table, start :Tile):
    a = set()
    t = [
        Tile(start.x+1, start.y),
        Tile(start.x-1, start.y),
        Tile(start.x, start.y+1),
        Tile(start.x, start.y-1),
    ]
    
    for tile in t:
        if tile.x < 0 or tile.y < 0:
            continue
        if tile.x > len(table[0]) or tile.y > len(table):
            continue
        if start in neighbors_per_follow(table, tile):
            # print(Tile(x, y))
            a.add(tile)

    return a

def around_start_direction(table, start :Tile):
    a = set()
    t = {
        'r':Tile(start.x+1, start.y),
        'l':Tile(start.x-1, start.y),
        'd':Tile(start.x, start.y+1),
        'u':Tile(start.x, start.y-1)
    }
    
    for key, tile in t.items():
        if tile.x < 0 or tile.y < 0:
            continue
        if tile.x > len(table[0]) or tile.y > len(table):
            continue
        if start in neighbors_per_follow(table, tile):
            # print(Tile(x, y))
            a.add(key)

    return a

def convert_directions(tile:Tile, direction):
    if direction == "r":
        return Tile(tile.x+1, tile.y)
    elif direction == "l":
        return Tile(tile.x-1, tile.y)
    elif direction == "d":
        return Tile(tile.x, tile.y+1)
    elif direction == "u":
        return Tile(tile.x, tile.y-1)
    return tile

def next_tile(table, tile :Tile, old :Tile):
    n = list(neighbors_per_follow(table, tile))
    n.remove(old)
    n = n[0]
    return n, tile

def primo(table, directions = None, stampa = True):
    start = starting_tile(table)
    o1, o2 = start, start
    if directions == None:
        t1, t2 = around_start(table, start)
    else:
        t1 = convert_directions(start, directions.pop())
        t2 = convert_directions(start, directions.pop())

    c = 1
    queue = set()
    queue.add(start)
    queue.add(t1)
    queue.add(t2)

    while t1 != t2:
        queue.add(t1)
        queue.add(t2)
        t1, o1 = next_tile(table, t1, o1)
        t2, o2 = next_tile(table, t2, o2)

        c+=1
    
    if stampa: print(c)
    return queue

def bfs(table, start):
    queue = deque()
    queue.append(start)
    visited = set()
    # visited.add(start)

    while queue:
        tile = queue.popleft()
        x, y = tile.x, tile.y
        if x < 0 or y < 0 or x >= len(table[0]) or y >= len(table):
            continue
        if table[y][x] != ".":
            continue
        table[y][x] = "X"

        neighbors = [
            Tile(x+1, y),
            Tile(x-1, y),
            Tile(x, y+1),
            Tile(x, y-1)
        ]
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                # visited.add(neighbor)

def dfs(table, tile:Tile):
    if tile.x < 0 or tile.y < 0:
        return
    if tile.x >= len(table[0]) or tile.y >= len(table):
        return
    if table[tile.y][tile.x] != ".":
        return
    table[tile.y][tile.x] = "X"
    dfs(table, Tile(tile.x+1, tile.y))
    dfs(table, Tile(tile.x-1, tile.y))
    dfs(table, Tile(tile.x, tile.y+1))
    dfs(table, Tile(tile.x, tile.y-1))


def secondo():
    table = read_file()
    directions = around_start_direction(table, starting_tile(table))
    print(directions)
    print("Tabella originaria:    ", len(table), len(table[0]))
    table = enlarge_table(table)
    print("Tabella allargata:     ", len(table), len(table[0]))
    
    queue = primo(table, directions, False)
    for x in range(len(table)):
        for y in range(len(table[x])):
            if Tile(x, y) not in queue:
                table[y][x] = "."
            else:
                queue.remove(Tile(x, y))
    
    bfs(table, Tile(0,0))

    table = reduce_table(table)
    print("Tabella rimpicciolita: ", len(table), len(table[0]))
    save_file(table)

    c = 0
    for y in range(len(table)):
        for x in range(len(table[y])):
            if table[y][x] == ".":
                c+=1
    print("Numero di caselle interne al percorso:", c)



def main():
    # primo(read_file())
    secondo()


if __name__ == "__main__":
    main()