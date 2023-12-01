import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "file.txt"


def main():
    board = [[1]]
    count = 1
    cords = [{'x':0, 'y':0}, {'x':0, 'y':0}]
    index = 1
    with open(FILE, "r") as f:
        data = f.read().strip()
        for c in data:

            index = (index +1 )% 2

            if c == "^":
                cords[index]['y'] -= 1
            elif c == "v":
                cords[index]['y'] += 1
            elif c == ">":
                cords[index]['x'] += 1
            elif c == "<":
                cords[index]['x'] -= 1
            

            if cords[index]['y'] >= len(board): # sto andnado verso il basso
                board.append([0] * len(board[0]))
            elif cords[index]['y'] < 0 :
                board.insert(0, [0] * len(board[0]))
                cords[0]['y']+=1
                cords[1]['y']+=1
            elif cords[index]['x'] >= len(board[0]):
                for i in range(len(board)):
                    board[i].append(0)
            elif cords[index]['x'] < 0:
                for i in range(len(board)):
                    board[i].insert(0, 0)
                cords[0]['x']+=1
                cords[1]['x']+=1


            if board[cords[index]['y']][cords[index]['x']] == 0:
                count += 1
            board[cords[index]['y']][cords[index]['x']] += 1

    for i in range(len(board)):
        print(board[i])
    print()
    print(count)
            




if __name__ == "__main__":
    main()