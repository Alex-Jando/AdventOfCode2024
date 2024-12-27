with open("input.txt", "r") as f:
    data = f.read()
    grid, instructions = data.split("\n\n")
    grid = [[c for c in line] for line in grid.splitlines()]
    instructions = instructions.replace("\n", "")

R, C = len(grid), len(grid[0])

stretchedGrid = []

for row in range(R):
    stretchedGrid.append([])
    for col in range(C):
        if grid[row][col] == "O":
            stretchedGrid[row].append("[")
            stretchedGrid[row].append("]")
        elif grid[row][col] == "#":
            stretchedGrid[row].append("#")
            stretchedGrid[row].append("#")
        elif grid[row][col] == "@":
            stretchedGrid[row].append("@")
            stretchedGrid[row].append(".")
        else:
            stretchedGrid[row].append(".")
            stretchedGrid[row].append(".")

grid = stretchedGrid

R, C = len(grid), len(grid[0])

x, y = None, None

for row in range(R):
    for col in range(C):
        if grid[row][col] == "@":
            x, y = row, col
            break

directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

for instruction in instructions:
    dr, dc = directions[instruction]
    spacesToMove = [(x, y)]
    checkedSpaces = 0
    hitWall = False
    while checkedSpaces < len(spacesToMove):
        r, c = spacesToMove[checkedSpaces]
        nr, nc = r + dr, c + dc
        if grid[nr][nc] in "[]":
            if (nr, nc) not in spacesToMove:
                spacesToMove.append((nr, nc))
            if grid[nr][nc] == "[":
                if (nr, nc + 1) not in spacesToMove:
                    spacesToMove.append((nr, nc + 1))
            if grid[nr][nc] == "]":
                if (nr, nc - 1) not in spacesToMove:
                    spacesToMove.append((nr, nc - 1))
        elif grid[nr][nc] == "#":
            hitWall = True
            break
        checkedSpaces += 1

    if hitWall:
        continue
    
    new_grid = [[grid[row][col] for col in range(C)] for row in range(R)]
    for r, c in spacesToMove:
        new_grid[r][c] = "."
    for r, c in spacesToMove:
        new_grid[r + dr][c + dc] = grid[r][c]

    grid = new_grid

    x, y = x + dr, y + dc

ans = 0

for row in range(R):
    for col in range(C):
        if grid[row][col] == "[":
            ans += row * 100 + col

print(ans)