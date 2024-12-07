with open("input.txt") as f:
    grid = [[s for s in line.strip()] for line in f.readlines()]

R = len(grid)
C = len(grid[0])

start = None

for row in range(R):
    for col in range(C):
        if grid[row][col] == "^":
            start = (row, col)
            break
    if start:
        break


def isLoop():
    pos = start

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    direction = 0

    visited = {(start, direction)}

    while True:
        row, col = pos
        dr, dc = directions[direction]
        if row + dr >= R or row + dr < 0 or col + dc >= C or col + dc < 0:
            break
        if grid[row + dr][col + dc] == "#":
            if direction + 1 > 3:
                direction = 0
            else:
                direction += 1
            continue
        if ((row + dr, col + dc), direction) in visited:
            return True
        pos = (row + dr, col + dc)
        visited.add((pos, direction))

    return False


loopCounter = 0

for row in range(R):
    for col in range(C):
        if grid[row][col] == ".":
            grid[row][col] = "#"
            if isLoop():
                loopCounter += 1
            grid[row][col] = "."

print(loopCounter)