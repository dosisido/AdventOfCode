from collections import deque
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
MOVES = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}
EX_MOVES = ['R', 'D', 'L', 'U']

table = [tuple(e if i!=1 else int(e) for i, e in enumerate(line.strip().split())) for line in open("file.txt", 'r')]

# print(x for x in table)

def dft(r, c, board):

    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        if board[r][c] == '#': continue
        board[r][c] = '#'
        for dr, dc in MOVES.values():
            nr = r + dr
            nc = c + dc
            if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] != '#':
                queue.append((nr, nc))



board = [['#']]
r, c = 0, 0
index = 0
for dir, n, ex in table:
    print('Riga elaborata:', index+1)
    index+=1

    # part 2
    # ex = ex[2:-1]
    # n = int(ex[0:5], 16)
    # dir = EX_MOVES[int(ex[5])]

    dr, dc = MOVES[dir]
    nr = r + (dr * n)
    nc = c + (dc * n)
    
    while nr<0:
        board.insert(0, ['.' for _ in range(len(board[0]))])
        nr += 1
        r+=1
    while nc<0:
        for row in board:
            row.insert(0, '.')
        nc += 1
        c+=1
    while nr>=len(board):
        board.append(['.' for _ in range(len(board[0]))])
    while nc>=len(board[0]):
        for row in board:
            row.append('.')
    for i in range(n):
        r += dr
        c += dc
        board[r][c] = '#'


# print('\n'.join(''.join(row) for row in board))
# with open("output.txt", 'w') as f:
#     f.write('\n'.join(''.join(row) for row in board))
        
for row in range(len(board)):
    isInside = False
    for cols in range(len(board[row])):
        if board[row][cols] == '#' and not isInside:
            isInside = True
            dft(row, cols+1, board)
            break

# dft(18, 246, board)
# print([[1 if x=='#' else 0 for x in row] for row in board])
print(sum(list(map(sum ,[[1 if x=='#' else 0 for x in row] for row in board]))))
# print()
# print('\n'.join(''.join(row) for row in board))