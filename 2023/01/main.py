import os

FILE = 'file.txt'
OUTPUT = 'output.txt'
CHAR = 50
DIGITS = ['_', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TO_REPLACE = [
    ('o1e', 'one'),
    ('t2o', 'two'),
    ('th3ee', 'three'),
    ('fo4ur', 'four'),
    ('fi5ve', 'five'),
    ('si6x', 'six'),
    ('se7ven', 'seven'),
    ('ei8ght', 'eight'),
    ('ni9ne', 'nine'),
    
]
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def find_numbers(word):
    a = None
    b = None
    for i in enumerate(word.strip()):
        if i[1].isnumeric():
            if a is None:
                a = i[1]
            b = i[1]
    return int(a+b)

def sum1():
    sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            sum+=find_numbers(line)
    return sum

def min_index(word):
    min_index = 999
    min_value = None
    for i in enumerate(DIGITS):
        try:
            index = word.index(i[1])
            if index < min_index:
                min_index = index
                min_value = i[0]
        except: pass
    return min_value


def convert_to_number(word):
    while True:
        number = min_index(word)
        if number is None: break
        word = word.replace(DIGITS[number], str(number))
    return word

def replace(word):
    for i in TO_REPLACE:
        word = word.replace(i[1], i[0])
    return word

def append_to_file(word):
    with open(OUTPUT, 'a') as f:
        f.write(word+'\n')

def sum2():
    with open(OUTPUT, 'w'): pass

    sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            word = replace(line)
            n = find_numbers(word)
            # print(n, line, word, sep=' - ')
            append_to_file(f"{n} - {line.ljust(CHAR)} - {word.ljust(CHAR)}")
            # input()
            sum+=n
    return sum


def main():
    
    # print(sum1())
    print(sum2())

if __name__ == "__main__":
    main()