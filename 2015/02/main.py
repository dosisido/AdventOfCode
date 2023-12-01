import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

FILE = 'file.txt'

def wrapping_paper():
    sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            x, y, z = line.strip().split('x')
            a = int(x) * int(y)
            b = int(y) * int(z)
            c = int(z) * int(x)
            m = min(a, b, c)
            sum += 2 * (a + b + c) + m
    print(sum)

def ribbon():
    sum = 0
    with open(FILE, 'r') as f:
        for line in f:
            x, y, z = line.strip().split('x')
            arr = [int(x), int(y), int(z)]
            arr.sort()
            sum+= 2 * (arr[0] + arr[1]) + arr[0] * arr[1] * arr[2]

    print(sum)


def main():
    ribbon()


if __name__ == "__main__":
    main()