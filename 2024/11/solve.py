from functools import cache
INPUT = "28591 78 0 3159881 4254 524155 598 1"

@cache
def apply_rule(x: int) -> list[int]:
    if x == 0:
        return [1]
    if len(str(x)) %2 == 0:
        return [
           int(str(x)[0:len(str(x))//2]),
           int(str(x)[len(str(x))//2:]),
        ]
    return [x * 2024]

@cache
def calcola(el, iter):
    n = apply_rule(el)
    if iter == 1:
        return len(n)

    return sum([calcola(x, iter - 1) for x in n])


rounds = 75
print(f"part2: {sum([calcola(x, rounds) for x in list(map(int, INPUT.split()))])}")