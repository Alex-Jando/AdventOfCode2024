from collections import deque


with open("input.txt") as f:
    grid = [[c for c in line if c != "\n"] for line in f.readlines()]

R = len(grid)
C = len(grid[0])

WORD = "MAS"

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
                    queue.append([{(r, c)}, (r, c), (dr, dc), (nr, nc)])

mas_occurences = []

while queue:
    visited, (r, c), (dr, dc), (mr, mc) = queue.popleft()
    if len(visited) == len(WORD):
        mas_occurences.append([(mr, mc), (dr, dc)])
        continue
    nr, nc = r + dr, c + dc
    if (
        0 <= nr < R
        and 0 <= nc < C
        and grid[nr][nc] == WORD[len(visited)]
        and (nr, nc) not in visited
    ):
        queue.append([visited | {(nr, nc)}, (nr, nc), (dr, dc), (mr, mc)])

xmas_occurences = 0

while mas_occurences:
    (mr1, mc1), (dr1, dc1) = mas_occurences.pop()
    to_rm = []
    for i in range(len(mas_occurences)):
        (mr2, mc2), (dr2, dc2) = mas_occurences[i]
        if mr1 == mr2 and mc1 == mc2:
            if dr1 == 0 and dc1 != 0:
                if dr1 * -1 == dr2 and 0 == dc2:
                    xmas_occurences += 1
                    to_rm.append(i)
                    continue
            if dr1 != 0 and dc1 == 0:
                if 0 == dr2 and -dc1 == dc2:
                    xmas_occurences += 1
                    to_rm.append(i)
                    continue
            if dr1 != 0 and dc1 != 0:
                if (dr1 == dr2 and -dc1 == dc2) or (-dr1 == dr2 and dc1 == dc2):
                    xmas_occurences += 1
                    to_rm.append(i)
                    continue
    for i in to_rm:
        mas_occurences.pop(i)

print(xmas_occurences)
