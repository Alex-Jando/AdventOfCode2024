from collections import deque

with open("input.txt", "r") as f:
    data = f.read()

grid = [[int(num) for num in line.strip()] for line in data.split("\n")]

R = len(grid)
C = len(grid[0])

queue = deque()

trail_ends = set()

for row in range(R):
    for col in range(C):
        if grid[row][col] == 0:
            queue.append([{(row, col)}, (row, col), (row, col), 0])

while queue:
    visited, trailhead, (row, col), height = queue.popleft()

    if grid[row][col] == 9:
        trail_ends.add((trailhead, (row, col)))
        continue

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc

        if (
            0 <= new_row < R
            and 0 <= new_col < C
            and grid[new_row][new_col] == height + 1
            and (new_row, new_col) not in visited
        ):
            queue.append(
                [
                    visited | {(new_row, new_col)},
                    trailhead,
                    (new_row, new_col),
                    height + 1,
                ]
            )

print(len(trail_ends))
