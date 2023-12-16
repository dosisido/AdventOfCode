import os
import copy
from collections import deque
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "file.txt"

DIRECTIONS = ['N', 'E', 'S', 'W']

def read_file():
    t = None
    with open(FILE, 'r') as f:
        t = tuple([tuple(line.strip()) for line in f.readlines()])
    
    b = []
    for i in range(len(t)):
        r = []
        for j in range(len(t[0])):
            r.append([])
        b.append(r)

    # print(len(t), len(t[0]), len(b), len(b[0]))
    return t, b

def print_table(board, x, y):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == y and j == x: print('X', end='')
            else: print(board[i][j], end='')
        print()

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if len(board[i][j]) == 0: print('.', end='')
            else:print('X', end='')
        print()

def where_I_go(tile, direction):
    if tile == '/':
        if direction == 'N': return ['W']
        if direction == 'W': return ['N']
        if direction == 'E': return ['S']
        if direction == 'S': return ['E']
    elif tile == '\\':
        if direction == 'N': return ['E']
        if direction == 'E': return ['N']
        if direction == 'S': return ['W']
        if direction == 'W': return ['S']
    elif tile == '|':
        if direction == 'N': return ['S']
        if direction == 'S': return ['N']
        if direction == 'E': return ['N', 'S']
        if direction == 'W': return ['N', 'S']
    elif tile == '-':
        if direction == 'N': return ['E', 'W']
        if direction == 'S': return ['E', 'W']
        if direction == 'E': return ['W']
        if direction == 'W': return ['E']
    else:
        if direction == 'N': return ['S']
        if direction == 'S': return ['N']
        if direction == 'E': return ['W']
        if direction == 'W': return ['E']

def translate_coming_from(direction_going_to, x, y):
    if direction_going_to == 'N': return (x, y - 1, 'S')
    if direction_going_to == 'S': return (x, y + 1, 'N')
    if direction_going_to == 'E': return (x + 1, y, 'W')
    if direction_going_to == 'W': return (x - 1, y, 'E')

def move_recursive(table, board, x, y, direction_coming_from):
    if x < 0 or x >= len(table[0]) or y < 0 or y >= len(table): return 

    # print_table(table, x, y)
    # print()
    if direction_coming_from in board[y][x]: return
    else: board[y][x].append(direction_coming_from)

    to_go = where_I_go(table[y][x], direction_coming_from)
    for direction in to_go:
        new_x, new_y, new_direction = translate_coming_from(direction, x, y)
        move_recursive(table, board, new_x, new_y, new_direction)

def move_queue(table, board, x, y, direction_coming_from):
    q = deque()
    q.append((x, y, direction_coming_from))

    while len(q) > 0:
        x, y, direction_coming_from = q.popleft()
        if x < 0 or x >= len(table[0]) or y < 0 or y >= len(table): continue

        if direction_coming_from in board[y][x]: continue
        else: board[y][x].append(direction_coming_from)

        to_go = where_I_go(table[y][x], direction_coming_from)
        for direction in to_go:
            new_x, new_y, new_direction = translate_coming_from(direction, x, y)
            q.append((new_x, new_y, new_direction))

def valuta_board(board):
    s = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if len(board[i][j]) != 0: s += 1
    return s

def primo():
    table, board = read_file() 

    move_queue(table, board, 0, 0, 'W')
    # print_board(board)
    
    s = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if len(board[i][j]) != 0: s += 1
        
    print(s)

def secondo():
    table, board = read_file() 

    moves = []
    for i in range(len(board)):
        moves.append((i, 0, 'N'))
        moves.append((i, len(board)-1, 'S'))
    for i in range(len(board[0])):
        moves.append((0, i, 'W'))
        moves.append((len(board[0])-1, i, 'E'))
    
    m = 0
    for x, y, direction in moves:
        b = copy.deepcopy(board)
        move_queue(table, b, x, y, direction)
        r = valuta_board(b)
        # print(r)
        m = max(m, r)
    print(m)


def main():
    # primo()
    secondo()

if __name__ == "__main__":
    main()