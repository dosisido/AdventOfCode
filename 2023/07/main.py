import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = "file.txt"

CHAR_chall1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]
CHAR_chall2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]

def read_file():
    l = []
    with open(FILE, "r") as f:
        for line in f:
            l.append((line.strip().split()))
    return l

"""
6    Five of a kind      where all five cards have the same label: AAAAA
5    Four of a kind      where four cards have the same label and one card has a different label: AA8AA
4    Full house          where three cards have the same label, and the remaining two cards share a different label: 23332

3    Three of a kind     where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
2    Two pair            where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
1    One pair            where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
0    High card           where all cards' labels are distinct: 23456
"""
TYPES = {
    6: "Five of a kind",
    5: "Four of a kind",
    4: "Full house",
    3: "Three of a kind",
    2: "Two pair",
    1: "One pair",
    0: "High card"
}

def poker(a:str):
    d = {}
    for i in a:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    # sono tutti diversi
    if len(d) == 5: return 0
    if len(d) == 4: return 1
    if len(d) == 3:
        if 3 in d.values(): return 3
        else: return 2
    # due tipi di carte: AAABB | AAAAB
    if len(d) == 2: 
        if 4 in d.values(): return 5
        else: return 4
    # sono tutti uguali
    if len(d) == 1: return 6

    exit("WTF")
    
def poker_jolly(b:str):
    a = str(b)
    d = {}
    for i in a:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    
    if 'J' in d.keys():
        n = d['J']
        if n == 5: return 6
        d.pop('J')

        max_index = list(d.keys())[0]
        for i in d.keys():
            if d[i]>d[max_index]:
                max_index = i
        d[max_index] += n

    # print(d)



    # sono tutti diversi
    if len(d) == 5: return 0
    if len(d) == 4: return 1
    if len(d) == 3:
        if 3 in d.values(): return 3
        else: return 2
    # due tipi di carte: AAABB | AAAAB
    if len(d) == 2: 
        if 4 in d.values(): return 5
        else: return 4
    # sono tutti uguali
    if len(d) == 1: return 6

    exit("WTF")


def riso(l:list, f, CHAR, prnt):
    def compp(x):
        x = x[0]
        it_er = 10
        val = 0
        for char in x:
            index = CHAR.index(char)
            val += index * 10**it_er
            it_er-=2
        return val
            

    d = {}

    for el in l:
        val = f(el[0])
        if val not in d.keys():
            d[val] = []
        d[val].append(el)
    
    # print(d)

    for k in d.keys():
        d[k].sort(key=compp)


    if prnt: 
        for k in range(7):
            if k in d.keys():
                print(TYPES[k], ':', sep='')
                for el in d[k]:
                    print("\t", el, sep='')

    prod = 1
    val = 0
    for k in range(7):
        if k in d.keys():
            for el in d[k]:
                val += prod * int(el[1])
                prod+=1

    print(val)

def main():
    l = read_file()
    # print(l)
    
    # for i in l:
    #     print(i[0], TYPES[poker(i[0])])

    # riso(l, poker, CHAR_chall1, false)
    riso(l, lambda x: max(poker(x), poker_jolly(x)), CHAR_chall2, False)

if __name__ == "__main__":
    main()