from collections import deque

with open("input.txt") as f:
    grid = [[c for c in line if c != "\n"] for line in f.readlines()]

R = len(grid)
C = len(grid[0])

WORD = "XMAS"

queue = deque()

for r in range(R):
    for c in range(C):
        if grid[r][c] == WORD[0]:
            for dr, dc in (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
                (1, 1),
                (1, -1),
                (-1, 1),
                (-1, -1),
            ):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                if grid[nr][nc] == WORD[1]:
                    queue.append([{(r, c)}, (r, c), (dr, dc)])

occurences = 0

while queue:
    visited, (r, c), (dr, dc) = queue.popleft()
    if len(visited) == len(WORD):
        occurences += 1
        continue
    nr, nc = r + dr, c + dc
    if (
        0 <= nr < R
        and 0 <= nc < C
        and grid[nr][nc] == WORD[len(visited)]
        and (nr, nc) not in visited
    ):
        queue.append([visited | {(nr, nc)}, (nr, nc), (dr, dc)])

print(occurences)
