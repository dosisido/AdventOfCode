import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import re

FILE = 'input.txt'

def first():
    RED = 12
    GREEN = 13
    BLUE = 14

    sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            flag = True
            line = line.strip()
            index = int(line.split(':')[0].split(' ')[1])
            for game in line.split(':')[1].split(';'):
                game = game.strip()
                # print(game.strip())
                g = re.search(r"([0-9]{0,2}) green", game)
                b = re.search(r"([0-9]{0,2}) blue", game)
                r = re.search(r"([0-9]{0,2}) red", game)

                if g and int(g.group(1)) > GREEN:
                    flag = False
                    break
                if b and int(b.group(1)) > BLUE:
                    flag = False
                    break
                if r and int(r.group(1)) > RED:
                    flag = False
                    break
            if flag:
                print(index)
                sum += index
    
    print(sum)


def second():
    sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            blue = 0
            green = 0
            red = 0

            line = line.strip()
            index = int(line.split(':')[0].split(' ')[1])
            for game in line.split(':')[1].split(';'):
                game = game.strip()
                g = re.search(r"([0-9]{0,2}) green", game)
                b = re.search(r"([0-9]{0,2}) blue", game)
                r = re.search(r"([0-9]{0,2}) red", game)

                if g:
                    green = max(green, int(g.group(1)))
                if b :
                    blue = max(blue, int(b.group(1)))
                if r:
                    red = max(red, int(r.group(1)))

            s = red * green * blue
            print(s)
            sum += s
    
    print(sum)

def main():
    second()


if __name__ == "__main__":
    main()