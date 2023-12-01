import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = 'file.txt'

def check(word):
    vowels = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
    if vowels < 3: return False
    if 'ab' in word or 'cd' in word or 'pq' in word or 'xy' in word : return False
    c = None
    for i in word:
        if c == i: return True
        c = i
    return False

def check2(word):
    def subf1(word):
        c = None
        for i in word:
            if c is not None: 
                if word.count(c+i) > 1: return True
            c = i
        return False

    def subf2(word):
        b = None
        c = None
        for a in word:
            if b is not None and c is not None:
                if c == a: return True
            c = b
            b = a
        return False


    return subf1(word) and subf2(word)

def main():
    sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            sum += 1 if check2(line) else 0
    print(sum)


if __name__ == "__main__":
    main()