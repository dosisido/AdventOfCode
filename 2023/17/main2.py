# fatto sguendo un tutorial su youtube
import os
from heapq import heappush, heappop
os.chdir(os.path.dirname(os.path.abspath(__file__)))

grid = [list(map(int, line.strip())) for line in open('file.txt', 'r') ]
R = len(grid)
C = len(grid[0])

pq = [(
    0,      # heat loss
    0,      # r
    0,      # c
    0,      # directon r
    0,      # direction c       (0,0) => standing still
    0       # n steps
)]

seen = set()

while pq:
    loss, r, c, dr, dc, n = heappop(pq)
    # print(r, c, loss, n, '|', dr, dc)

    if r == R-1 and c == C-1 and n>=4:
        print(loss)
        break

    if (r, c, dr, dc, n) in seen:
        continue
    seen.add((r, c, dr, dc, n))

    # continue in the same direction
    if n < 10 and (dr, dc) != (0, 0):
        nr = r + dr
        nc = c + dc
        if 0<=nr<R and 0<=nc<C:
            heappush(pq, (loss + grid[nr][nc], nr, nc, dr, dc, n+1))

    # change direction
    if n>=4 or (dr, dc) == (0, 0):
        for ndr, ndc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):    
                nr = r + ndr
                nc = c + ndc
                if 0<=nr<R and 0<=nc<C:
                    heappush(pq, (loss + grid[nr][nc], nr, nc, ndr, ndc, 1))