import os

FILE = 'file.txt'
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    floor = 0
    i = 0
    with open(FILE, 'r') as f:
        for c in f.read():
            i+=1
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1
            if floor == -1:
                print('Basement at: ', i)
                exit()
    print(floor)


if __name__ == "__main__":
    main()