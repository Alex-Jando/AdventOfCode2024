with open("input.txt") as f:
    lines = f.readlines()

S = 0

for line in lines:
    levels = [int(n) for n in line.split()]
    try:
        direction = (levels[1] - levels[0]) / abs(levels[1] - levels[0])
    except ZeroDivisionError:
        # Occurs if there is no change and therefore no directions
        # Meaning that this is an unsafe report
        continue
    if direction == 1:
        for i in range(1, len(levels) - 1):
            if levels[i] - levels[i - 1] not in {1, 2, 3} or levels[i] - levels[
                i + 1
            ] not in {-1, -2, -3}:
                break
        else:
            S += 1
    else:
        for i in range(1, len(levels) - 1):
            if levels[i] - levels[i - 1] not in {-1, -2, -3} or levels[i] - levels[
                i + 1
            ] not in {1, 2, 3}:
                break
        else:
            S += 1

print(S)
