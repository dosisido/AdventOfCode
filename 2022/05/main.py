FILE_IN = "05/input.txt"

#                         [Z] [W] [Z]
#         [D] [M]         [L] [P] [G]
#     [S] [N] [R]         [S] [F] [N]
#     [N] [J] [W]     [J] [F] [D] [F]
# [N] [H] [G] [J]     [H] [Q] [H] [P]
# [V] [J] [T] [F] [H] [Z] [R] [L] [M]
# [C] [M] [C] [D] [F] [T] [P] [S] [S]
# [S] [Z] [M] [T] [P] [C] [D] [C] [D]
#  1   2   3   4   5   6   7   8   9 
arr = [
    [],
    ['S', 'C', 'V', 'N'],
    ['Z', 'M', 'J', 'H', 'N', 'S'],
    ['M', 'C', 'T', 'G', 'J', 'N', 'D'],
    ['T', 'D', 'F', 'J', 'W', 'R', 'M'],
    ['P', 'F', 'H'],
    ['C', 'T', 'Z', 'H', 'J'],
    ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'],
    ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'],
    ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z']
]

def main():

    with open(FILE_IN, 'r') as f:
        for line in f:
            line = line.strip().split() # move $0 from $1 to $2
            line = [
                int(line[0]),
                int(line[1]),
                int(line[2])
            ]
            tmp = []
            for i in range(line[0]):
                el = arr[line[1]][-1]
                arr[line[1]].pop(len(arr[line[1]])-1)
                tmp.append(el)
            for i in range(line[0]-1, -1, -1):
                arr[line[2]].append(tmp[i])

    for i in range(1, len(arr)):
        print(arr[i][-1], end='')

if __name__ == "__main__":
    main()