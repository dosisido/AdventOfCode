import os
from heapq import heappush, heappop, heapify
from collections import deque
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = 'file.txt'

DIRECTIONS = ['N', 'E', 'S', 'W']

class PQ_item:
    def __init__(self, x:int, y:int, weight:int, straight:int, direction:str):
        self.x = x
        self.y = y
        self.weight = weight
        self.straight = straight
        self.direction = direction

    def __lt__(self, other):
        return self.weight < other.weight
    def __le__(self, other):
        return self.weight <= other.weight
    
    def __gt__(self, other):
        return self.weight > other.weight
    def __ge__(self, other):
        return self.weight >= other.weight
    
    def __eq__(self, other):
        return self.weight == other.weight
    def __ne__(self, other):
        return self.weight != other.weight

    def __str__(self):
        return f'{"{"} (r:{self.y}, c:{self.x}), w:{self.weight}, s:{self.straight}, d:{self.direction} {"}"}'

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.weight, self.straight, self.direction))



def read_file():
    t = []
    with open(FILE, 'r') as f:
        for line in f:
            t.append(tuple(int(x) for x in line.strip()))
    return tuple(t)

def print_H(heap):
    for i in heap:
        print(i, end=' ')
    print()

def possibilities(table, item:PQ_item):
    dirs = deque()
    
    if item.straight<3:
        dirs.append((item.direction, item.straight+1))
    
    if item.direction == 'N':
        dirs.append(('W', 1))
        dirs.append(('E', 1))
    elif item.direction == 'E':
        dirs.append(('N', 1))
        dirs.append(('S', 1))
    elif item.direction == 'S':
        dirs.append(('W', 1))
        dirs.append(('E', 1))
    elif item.direction == 'W':
        dirs.append(('N', 1))
        dirs.append(('S', 1))

    r = []
    while dirs:
        d = dirs.pop()
        if d[0] == 'N':
            if item.y+1 >= len(table): continue
            r.append(PQ_item(item.x, item.y+1, item.weight + table[item.y+1][item.x], d[1], 'N'))
        elif d[0] == 'W':
            if item.x+1 >= len(table[0]): continue
            r.append(PQ_item(item.x+1, item.y, item.weight + table[item.y][item.x+1], d[1], 'W'))
        elif d[0] == 'S':
            if item.y-1 < 0: continue
            r.append(PQ_item(item.x, item.y-1, item.weight + table[item.y-1][item.x], d[1], 'S'))
        elif d[0] == 'E':
            if item.x-1 < 0: continue
            r.append(PQ_item(item.x-1, item.y, item.weight + table[item.y][item.x-1], d[1], 'E'))
    return r

def possibilities2(table, item:PQ_item):
    dirs = deque()
    
    if item.straight<10:
        dirs.append((item.direction, item.straight+1))
    
    if item.straight >= 4:
        if item.direction == 'N':
            dirs.append(('W', 1))
            dirs.append(('E', 1))
        elif item.direction == 'E':
            dirs.append(('N', 1))
            dirs.append(('S', 1))
        elif item.direction == 'S':
            dirs.append(('W', 1))
            dirs.append(('E', 1))
        elif item.direction == 'W':
            dirs.append(('N', 1))
            dirs.append(('S', 1))

    r = []
    while dirs:
        d = dirs.pop()
        if d[0] == 'N':
            if item.y+1 >= len(table): continue
            r.append(PQ_item(item.x, item.y+1, item.weight + table[item.y+1][item.x], d[1], 'N'))
        elif d[0] == 'W':
            if item.x+1 >= len(table[0]): continue
            r.append(PQ_item(item.x+1, item.y, item.weight + table[item.y][item.x+1], d[1], 'W'))
        elif d[0] == 'S':
            if item.y-1 < 0: continue
            r.append(PQ_item(item.x, item.y-1, item.weight + table[item.y-1][item.x], d[1], 'S'))
        elif d[0] == 'E':
            if item.x-1 < 0: continue
            r.append(PQ_item(item.x-1, item.y, item.weight + table[item.y][item.x-1], d[1], 'E'))
    return r

def primo():
    table = read_file()


    heap = [PQ_item(1, 0, table[0][1], 1, 'W'), PQ_item(0, 1, table[1][0], 1, 'N')]
    heapify(heap)

    visited = set()

    while heap:
        item = heappop(heap)
        x, y = item.x, item.y
        # print('Item:', item)
        # input()

        if (x, y, item.direction, item.straight) in visited:continue
        visited.add((x, y, item.direction, item.straight))

        # print('Heap: ', end='')
        # print_H(heap)

        if x == len(table[0])-1 and y == len(table)-1:  # terminazione
            print(item.weight)
            break

        r = possibilities(table, item)
        for i in r:
            heappush(heap, i)


    else:
        print('No path found')
        exit(1)
    
def secondo():
    table = read_file()


    heap = [PQ_item(1, 0, table[0][1], 1, 'W'), PQ_item(0, 1, table[1][0], 1, 'N')]
    heapify(heap)

    visited = set()

    while heap:
        item = heappop(heap)
        x, y = item.x, item.y
        # print('Item:', item)
        # input()

        if (x, y, item.direction, item.straight) in visited:continue
        visited.add((x, y, item.direction, item.straight))

        # print('Heap: ', end='')
        # print_H(heap)

        if x == len(table[0])-1 and y == len(table)-1:  # terminazione
            if item.straight < 4: continue
            print(item.weight)
            break

        r = possibilities2(table, item)
        for i in r:
            heappush(heap, i)


    else:
        print('No path found')
        exit(1)
 

def main():
    # primo()
    secondo()
    """ 
        875
      """
    pass

if __name__ == "__main__":
    main()