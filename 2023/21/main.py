import os
from collections import deque
os.chdir(os.path.dirname(os.path.abspath(__file__)))

table = [ [x for x in line.strip()] for line in open("file.txt", 'r')]
sr, sc = None, None
for r, row in enumerate(table):
    for c, char in enumerate(row):
        if char == 'S':
            sr, sc = r, c
            break
    if sr is not None and sc is not None: break

N = 64
queue = deque()
queue.append((sr, sc, 0))
pots = set()
i = 0
while queue:
    r, c, step = queue.popleft()
    if r<0 or r>=len(table) or c<0 or c>=len(table[0]): continue
    if table[r][c] == '#': continue
    if step > N: continue
    if step>i:
        i = step
        print(i)
    if step == N: pots.add((r, c))

    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r+dr, c+dc
        queue.append((nr, nc, step+1))

print(len(pots))
# print(pots)