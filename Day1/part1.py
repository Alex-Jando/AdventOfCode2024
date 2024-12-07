with open("input.txt") as f:
    lines = f.readlines()

T = 0

LIST_1 = []
LIST_2 = []

for line in lines:
    d1, d2 = map(int, line.split())
    LIST_1.append(d1)
    LIST_2.append(d2)

LIST_1.sort()
LIST_2.sort()

for d1, d2 in zip(LIST_1, LIST_2):
    T += abs(d1 - d2)

print(T)
