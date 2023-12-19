import os
from collections import deque
os.chdir(os.path.dirname(__file__))

b1, b2 = [], []
with open('file.txt') as f:
    lines = f.readlines()
    for line in lines: 
        if line.strip() == '': break
        b1.append(line.strip())
    for line in lines[len(b1)+1:]:
        b2.append(line.strip())

d = {}
for el in b1:
    e1, e2 = el.rstrip('}').split('{')
    d[e1] = e2.split(',')

b2 = b2.__str__().replace('=', ':').replace('\'', '').replace('x', "'x'").replace('m', "'m'").replace('a', "'a'").replace('s', "'s'")
b2 = eval(f'{b2}')

queue = deque()
for el in b2:
    queue.append(('in', el))

def evaluate(cond, el):
    x = el['x']
    m = el['m']
    a = el['a']
    s = el['s']
    return eval(cond)

A = []
# R = []
while queue:
    command, el = queue.popleft()
    cmd_line = d[command]
    for cmd in cmd_line:
        try:
            cond, dir = cmd.split(':')
            cond = evaluate(cond, el)
        except ValueError:
            cond = True
            dir = cmd
        if cond:
            if dir == 'A':
                A.append(el)
            elif dir == 'R':
                pass
                # R.append(el)
            else:
                queue.append((dir, el))
            break

s = 0
for el in A:
    s+= el['x']+el['m']+el['a']+el['s']
print(s)