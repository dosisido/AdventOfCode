import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = 'file.txt'

def count_number_of_occurrences(a, b):
    count = 0
    for i in b:
        if i in a:
            count += 1
    return count

def calcola(a, b):
    val = 1
    for i in b:
        if i in a:
            val*=2
    return 0 if val == 1 else val//2
    
def primo():
    sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            data = line.strip().split(':')[1].strip().split('|')
            v = calcola(data[0].strip().split(), data[1].strip().split())
            print(v)
            sum += v
    print(sum)

def secondo():
    data = []
    with open(FILE, 'r') as f:
        for line in f:
            row = line.strip().split(':')[1].strip().split('|')
            data.append([row[0].strip().split(), row[1].strip().split()])
            

    fifo = [ i for i in range(1, len(data)+1)]
    i = 0
    while i<len(fifo):
        # print(fifo)
        index = fifo[i] - 1
        n = count_number_of_occurrences(data[index][0], data[index][1])
        for j in range(n):
            fifo.append(index+2+j)
        i += 1

    print(len(fifo))

def main():
    secondo()




if __name__ == "__main__":
    main()