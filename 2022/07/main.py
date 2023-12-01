FILE_IN = "07/inputSimplified.txt"
FILE_IN = "07/input.txt"
N = 100000
FREE = 30000000 
# 8729145
HARD_DISK = 70000000

def findParent(data, path, name):
    for i in range(len(data)):
        if data[i][0] == path and data[i][1] == name and data[i][3] == 'dir':
            return i


def main():
    data = [] # path, name, element
    path = []
    with open(FILE_IN, "r") as f: 
        line = f.readline().strip()
        try:
            while True:
                if '$' in line:                             # comando
                    if "cd" in line:
                        line = line.split()
                        if ".." in line[-1]:
                            path.pop()
                        elif "/" in line[-1]:
                            path = []
                        else:
                            path.append(line[-1])
                        
                        line = f.readline().strip()
                        if line == '': break
                        
                    elif "ls" in line:
                        while True:
                            line = f.readline().strip()
                            if "$" in line or line == '':
                                break
                            else:
                                line = line.split()
                                if 'dir' in line:
                                    data.append(['/'.join(path), line[-1], 0, 'dir']) # elenco delle cartelle figlie(?)
                                else: 
                                    data.append(['/'.join(path), line[1], int(line[0]), 'file'])
                        pass
                if line == '': break
                

        except EOFError:
            pass
    
    print(data)

    data.reverse()
    with open("07/out.txt", 'w+') as f:
        for el in data:
            # print(el)
            f.write(str(el) + "\n")
    
    count = 0
    disk = 0
    for el in data:
        if el[0] != '':
            path = '/'.join(el[0].split('/')[0:-1])
            name = el[0].split('/')[-1]
            parentIndex = findParent(data, path, name)
            data[parentIndex][2] += el[2]
        else:
            disk += el[2]
        
        if el[3] == 'dir':
            if el[2] <= N:
                count += el[2]
    
    index = -1
    free = FREE - (HARD_DISK - disk)
    for el in data:
        if el[3] == 'dir':
            if el[2] >= free:
                if index == -1:
                    index = data.index(el)
                elif data[index][2] > el[2]:
                    index = data.index(el)


    with open("07/out.txt", 'w+') as f:
        for el in data:
            f.write(str(el) + "\n")

    print("Somma delle directory:", count)
    print("Indice:", index)
    print("Directory con più di", free, "byte:", data[index][2])

if __name__ == "__main__":
    main()