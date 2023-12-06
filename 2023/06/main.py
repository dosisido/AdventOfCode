import os
import math
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = 'file.txt'


def read_file():
    time = []
    distance = []

    with open(FILE, 'r') as f:
        lines = f.readlines()
        time = [int(x) for x in lines[0].split(':')[1].strip().split()]
        distance = [int(x) for x in lines[1].split(':')[1].strip().split()]
    
    return time, distance

def read_file_no_spaces():
    time = []
    distance = []

    with open(FILE, 'r') as f:
        lines = f.readlines()
        time = [int(x) for x in lines[0].split(':')[1].strip().replace(' ', '').split()]
        distance = [int(x) for x in lines[1].split(':')[1].strip().replace(' ', '').split()]
    
    return time, distance


def calcola_possibilita(time, distance):
    count = 0
    for sped in range(0, time+1):
        time_remaining = time - sped
        d = time_remaining * sped
        # print(d)
        if d>distance:
            count += 1
    return count-1

def calcola_possibilita_eq(time, distance, print_=False):
    delta = time**2 - 4*distance
    max = (time + math.sqrt(delta))/2
    min = (time - math.sqrt(delta))/2
    if print_: (max, min)
    if(max==float(math.floor(max))):
        max = math.floor(max)-1
    else:
        max = math.floor(max)
    
    if(min==float(math.ceil(min))):
        min = math.ceil(min)+1
    else:
        min = math.ceil(min)
    if print_: print(max, min)
    if print_: print(max-min+1) # quanti interi ci sono tra max e min
    return max-min+1

def primo():
    time, distance = read_file()
    # primo(time, distance)
    # print(time, distance)

    # calcola_possibilita_eq(time[2], distance[2])
    # exit()
    prod = 1
    for i in range(0, len(time)):
        prod*=calcola_possibilita_eq(time[i], distance[i])
    print(prod)

def secondo():
    time, distance = read_file_no_spaces()
    # primo(time, distance)
    # print(time, distance)

    # calcola_possibilita_eq(time[2], distance[2])
    # exit()
    prod = 1
    for i in range(0, len(time)):
        prod*=calcola_possibilita_eq(time[i], distance[i])
    print(prod)

def main():
    # primo()
    secondo()

if __name__ == "__main__":
    main()