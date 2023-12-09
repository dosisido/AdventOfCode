import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "file.txt"


def read_file():
    with open(FILE, "r") as file:
        for line in file:
            val =  [[int(x) for x in line.split()]]
            index = 1
            while True:
                val.append([])
                for i in range(1, len(val[index-1])):
                    n0 = val[index-1][i-1]
                    n1 = val[index-1][i]
                    val[index].append(n1-n0)
                print(val[index])
                
                if val[index].count(0) == len(val[index]):
                    break
                index += 1
            yield val


def primo():
    sum = 0
    for line in read_file():
        line[-1].append(0)
        for index in range(len(line)-2, -1, -1):
            line[index].append(line[index+1][-1] + line[index][-1])
            print(line[index])
        val = line[0][-1]
        sum += val
    print(sum)

def secondo():
    sum = 0
    for line in read_file():
        line[-1].insert(0, 0)
        for index in range(len(line)-2, -1, -1):
            line[index].insert(0, line[index][0] - line[index+1][0])
            print(line[index])
        val = line[0][0]
        sum += val
    print(sum)

def main():
    # primo()
    secondo()

if __name__ == "__main__":
    main()