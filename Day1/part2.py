from collections import Counter

with open("input.txt") as f:
    lines = f.readlines()

T = 0

LIST_1 = []
LIST_2 = []

for line in lines:
    d1, d2 = map(int, line.split())
    LIST_1.append(d1)
    LIST_2.append(d2)

LIST_2_OCCURENCES = Counter(LIST_2)

for n in LIST_1:
    T += n * LIST_2_OCCURENCES[n]

print(T)
