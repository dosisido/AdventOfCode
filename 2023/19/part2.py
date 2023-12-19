import os
from collections import deque
from copy import deepcopy
os.chdir(os.path.dirname(__file__))

def read_file():
    b1 = []
    with open('file.txt') as f:
        lines = f.readlines()
        for line in lines: 
            if line.strip() == '': break
            b1.append(line.strip())

    d = {}
    for el in b1:
        e1, e2 = el.rstrip('}').split('{')
        d[e1] = e2.split(',')
    return d
d = read_file()
intervals = {
    'in': [{
        'x': [1, 4000],
        'm': [1, 4000],
        'a': [1, 4000],
        's': [1, 4000]
    },]
}

queue = deque()
queue.append('in')

def find_letter(key):
    if 'x' in key: return 'x'
    if 'm' in key: return 'm'
    if 'a' in key: return 'a'
    if 's' in key: return 's'

while queue:
    key = queue.popleft()
    if key in ('A', 'R'): continue
    cmd_line = d[key]
    for cmd in cmd_line:
        try:
            cond, dir = cmd.split(':')
        except ValueError:
            cond = True
            dir = cmd

        if key in intervals.keys():
            if cond != True:
                mode = find_letter(cond)

                elements = intervals.pop(key)
                i = 0
                for el in elements:
                    v1 = deepcopy(el)
                    v2 = deepcopy(el)
                    v = el[mode]

                    sign = '>' if '>' in cond else '<'
                    index = int(cond.split(sign)[1])

                    if sign == '>':
                        v1[mode] = [v[0], index]
                        v2[mode] = [index+1, v[1]]
                    elif sign == '<':
                        v2[mode] = [v[0], index-1]
                        v1[mode] = [index, v[1]]
                    

                    if dir not in intervals.keys():
                        intervals[dir] = list()
                    if key not in intervals.keys():
                        intervals[key] = list()
                    intervals[dir].append(v2)
                    intervals[key].append(v1)

                    if dir not in queue: queue.append(dir)

            else:
                v = intervals.pop(key)
                if dir not in intervals.keys():
                    intervals[dir] = list()
                for el in v:
                    intervals[dir].append(el)
                if dir not in queue: queue.append(dir)


print("intervals['A']")
for el in intervals['A']:
    print('\t', el)
print("intervals['R']")
for el in intervals['R']:
    print('\t', el)

A = intervals['A']
s = 0
for el in A:
    s+= (el['x'][1]-el['x'][0]+1)*(el['m'][1]-el['m'][0]+1)*(el['a'][1]-el['a'][0]+1)*(el['s'][1]-el['s'][0]+1)
print(s)