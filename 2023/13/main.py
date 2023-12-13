from functools import cache
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "file.txt"

def read_file():
    with open(FILE, "r") as f:
        t = []
        for line in f:
            if line.strip() == "":
                yield t
                t = []
                continue
            else:
                # t.append(list([x for x in line.strip()]))
                t.append(line.strip())
        yield t


def find_simmetry_row(t, val = None):
    @cache
    def ceck(r1, r2) -> bool:
        if len(r1) * len(r2) == 0:
            return True
        if r1[-1] == r2[0]:
            return ceck(r1[0:-1], r2[1:])
        return False

    for i in range(1, len(t[0])):
        r = 0
        if ceck(t[r][:i], t[r][i:]):
            for r in range(1, len(t)):
                if not ceck(t[r][:i], t[r][i:]):
                    break
            else: 
                if val != i: return i
    return False

def find_simmetry_col(t, val = None):
    for r in range(0, len(t)-1):
        if t[r] == t[r+1]:
            for i in range(1, min((r, len(t)-1-(r+1)))+1):
                if t[r-i] != t[r+1+i]:
                    break
            else: 
                if r+1 != val: return r+1

    return False

def primo():
    s = 0
    i = 0
    for t in read_file():
        r = find_simmetry_row(t)
        if r:
            s+= r
            # print(f"Simmetry at {i} col {r}")
        else:
            c = find_simmetry_col(t)
            if c:
                s+= c*100
                # print(f"Simmetry at {i} row {c}")
            # else: print(f"No simmetry at {i}")
        i+=1
    return s

def simmetry(t, skip = None):
    l = set()
    if skip!=None and skip[0] == 'c':
        r = find_simmetry_row(t, skip[1])
    else:
        r = find_simmetry_row(t)
    if r:
        l.add(('c', r))
    if skip!=None and skip[0] == 'r':
        c = find_simmetry_col(t, skip[1])
    else:
        c = find_simmetry_col(t)
    if c:
        l.add(('r', c))

    return l

def secondo():
    s = 0
    for t in read_file():
        orig_set = simmetry(t)
        orig = set(orig_set).pop()
        l = set()
        for i in range(len(t)):
            for j in range(len(t[i])):
                t[i] = t[i][:j] + ('.' if t[i][j] == '#' else '#') + t[i][j+1:]
                simm = simmetry(t, orig)
                t[i] = t[i][:j] + ('.' if t[i][j] == '#' else '#') + t[i][j+1:]
                l = l.union(simm)
        l = l.difference(orig_set)
        print(l, orig_set)
        if len(l) == 1:
            a = l.pop()
            p, v = a
            if p == 'c':
                s+= v
            if p == 'r':
                s+= v*100
    print(s)

def main():
    primo()
    secondo()

if __name__ == "__main__":
    main()

"""
23657
54445
32006
"""