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

highest_id = FS[j]

while highest_id >= 0:
    id_length = []
    dot_count = 0

    for i in range(len(FS) - 1, 0, -1):
        if FS[i] != highest_id and id_length:
            break
        if FS[i] == highest_id:
            id_length.append(i)

    for i in range(id_length[0]):
        if FS[i] != ".":
            dot_count = 0
            continue
        dot_count += 1
        if dot_count == len(id_length):
            for k, n in enumerate(id_length):
                FS[i - dot_count + k + 1], FS[n] = FS[n], FS[i - dot_count + k + 1]
            break

    highest_id -= 1

CHECKSUM = 0

for i in range(len(FS)):
    if FS[i] == ".":
        continue
    CHECKSUM += FS[i] * i

print(CHECKSUM)
