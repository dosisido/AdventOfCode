IN_FILE = "./03/input.txt"

def value(val):
    return ord(val) - ord('A') + 27 if val.isupper() else ord(val) - ord('a') + 1

def main(): 
    count = 0
    with open(IN_FILE, "r") as f:
        for line1 in f:
            line2 = f.readline()
            line3 = f.readline()

            for el in line1:
                if el in line2 and el in line3:
                    count += value(el)
                    break
    
    print(count)

if __name__ == "__main__":
    main()