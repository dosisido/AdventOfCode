import os
import hashlib
os.chdir(os.path.dirname(os.path.abspath(__file__)))
STR = 'yzbqklnj'

def f(a):
    return a[0] == '0' and a[1] == '0' and a[2] == '0' and a[3] == '0' and a[4] == '0' and a[5] == '0'


def main():

    c = 0
    while True:
        c+=1
        a = hashlib.md5((STR + str(c)).encode()).hexdigest()
        if f(a):
            print(c)
            break

        if c % 1000000 == 0:
            print(c)

if __name__ == "__main__":
    main()