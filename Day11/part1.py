with open("input.txt") as f:
    data = f.read()

stones = [int(n) for n in data.strip().split()]


def blink(stones):
    s = 0
    max_s = len(stones)
    while s < max_s:
        if stones[s] == 0:
            stones[s] = 1
        elif len(str(stones[s])) % 2 == 0:
            l_digits, r_digits = (
                str(stones[s])[: len(str(stones[s])) // 2],
                str(stones[s])[len(str(stones[s])) // 2 :],
            )
            stones[s] = int(l_digits)
            stones.insert(s + 1, int(r_digits))
            s += 1
            max_s += 1
        else:
            stones[s] *= 2024
        s += 1


for i in range(25):
    blink(stones)

print(len(stones))
