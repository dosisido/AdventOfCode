import os
import re
from math import lcm
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "file.txt"


def read_file():
    sequence = None
    match = None
    with open(FILE, "r") as f:
        lines = f.readlines()
        sequence = lines[0].strip()
        match = re.findall(r"([A-Z0-9]{3})\D.*?=\D.*?\(([A-Z0-9]{3}),\D.*?([A-Z0-9]{3})\)", "\n".join(lines[2:]))
    sequence = [0 if x == 'L' else 1 for x in sequence]
    m = {}
    for a, b, c in match:
        m[a] = (b,c)
    return sequence, m

def path(sequence, tile, match):
    i = 0
    step = 0
    while tile != 'ZZZ':
        direction = sequence[i]
        tile = match[tile][direction]
        step += 1
        i = (i+1) % len(sequence)
    return step

def path2(sequence, tile, match):
    i = 0
    step = 0
    while not tile.endswith('Z'):
        direction = sequence[i]
        tile = match[tile][direction]
        step += 1
        i = (i+1) % len(sequence)
    return step

def primo(sequence, match):
    tile = 'AAA'
    step = path(sequence, tile, match)
    print(step)

def secondo(sequence, match):
    tiles = [x for x in match.keys() if x[2] == 'A']
    i = 0
    step = 0
    while len([x for x in tiles if x[2] != 'Z']) != 0:
        direction = sequence[i]
        exit = direction == 1

        for k in range(len(tiles)):
            tiles[k] = match[tiles[k]][direction]
            if exit and tiles[k][2] != 'Z':
                exit = False

        if exit: break
        step += 1
        i = (i+1) % len(sequence)
    print(step)

def seconodo_lcm(sequence, match):
    tiles = [x for x in match.keys() if x[2] == 'A']
    i = 0
    step = []
    for tile in tiles:
        step.append(path2(sequence, tile, match))

    print(step)
    print(lcm(*step))

def main():
    sequence, match = read_file()
    # primo(sequence, match)
    seconodo_lcm(sequence, match)
    
    pass

if __name__ == "__main__":
    main()