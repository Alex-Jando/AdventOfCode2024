with open("input.txt") as f:
    lines = f.readlines()

S = 0


def checkLevels(levels):
    try:
        direction = (levels[1] - levels[0]) / abs(levels[1] - levels[0])
    except ZeroDivisionError:
        # Occurs if there is no change and therefore no directions
        # Meaning that this is an unsafe report
        return False
    if direction == 1:
        for i in range(1, len(levels) - 1):
            if levels[i] - levels[i - 1] not in {1, 2, 3} or levels[i] - levels[
                i + 1
            ] not in {-1, -2, -3}:
                break
        else:
            return True
    else:
        for i in range(1, len(levels) - 1):
            if levels[i] - levels[i - 1] not in {-1, -2, -3} or levels[i] - levels[
                i + 1
            ] not in {1, 2, 3}:
                break
        else:
            return True

    return False


for line in lines:
    levels = [int(n) for n in line.split()]
    if checkLevels(levels):
        S += 1
    else:
        for potentiallyBad in range(len(levels)):
            if checkLevels(levels[:potentiallyBad] + levels[potentiallyBad + 1 :]):
                S += 1
                break


print(S)
