import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
table = [tuple(e if i!=1 else int(e) for i, e in enumerate(line.strip().split())) for line in open("file.txt", 'r')]
MOVES = {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}
EX_MOVES = ['R', 'D', 'L', 'U']

r, c = 0, 0
points = [(r, c)]
perimeter = 0

for dir, n, ex in table:
    # part 2
    ex = ex[2:-1]
    n = int(ex[0:5], 16)
    dir = EX_MOVES[int(ex[5])]

    dr, dc = MOVES[dir]
    r+= (dr * n)
    c+= (dc * n)
    
    points.append((r, c))
    perimeter += n

s1, s2 = 0, 0
for i in range(len(table)-1):
    s1+= points[i][0] * points[i+1][1]
    s2+= points[i][1] * points[i+1][0]

area = abs(s1 - s2) // 2
print(area)
print(perimeter)
print(area + perimeter//2 +1)               # PERCHé!?!

