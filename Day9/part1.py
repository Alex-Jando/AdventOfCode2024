with open("input.txt") as f:
    data = f.read().strip()

FS = []

index = 0

for i, num in enumerate(data):
    if i % 2 == 0:
        for _ in range(int(num)):
            FS.append(index)
        index += 1
    else:
        for _ in range(int(num)):
            FS.append(".")

i = 0
j = len(FS) - 1

while i < j:
    if FS[j] == ".":
        j -= 1
        continue
    if FS[i] == ".":
        FS[i], FS[j] = FS[j], FS[i]
        j -= 1
        i += 1
    else:
        i += 1

CHECKSUM = 0

for i in range(len(FS)):
    if FS[i] == ".":
        break
    CHECKSUM += FS[i] * (i)

print(CHECKSUM)
