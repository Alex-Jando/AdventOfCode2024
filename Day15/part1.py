with open("input.txt", "r") as f:
    data = f.read()
    grid, instructions = data.split("\n\n")
    grid = [[c for c in line] for line in grid.splitlines()]
    instructions = instructions.replace("\n", "")

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
    boxes = []
    nr, nc = x + dr, y + dc
    while grid[nr][nc] == "O":
        boxes.append((nr, nc))
        nr += dr
        nc += dc

    if grid[nr][nc] == "#":
        continue

    spacesToMove = [(x, y)] + boxes + [(nr, nc)]
    for (x1, y1), (x2, y2) in list(zip(spacesToMove, spacesToMove[1:]))[::-1]:
        grid[x2][y2] = grid[x1][y1]

    x, y = x + dr, y + dc

ans = 0

for row in range(R):
    for col in range(C):
        if grid[row][col] == "O":
            ans += row * 100 + col

print(ans)