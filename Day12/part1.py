from collections import deque

with open("input.txt") as f:
    lines = f.readlines()

grid = [[n for n in line.strip()] for line in lines]

R = len(grid)
C = len(grid[0])

cost = 0

visited = set()

for row in range(R):
    for col in range(C):
        if (row, col) in visited:
            continue
        item = grid[row][col]
        queue = deque([(row, col)])
        area = 0
        perimeter = 0
        while queue:
            (r, c) = queue.popleft()
            if (r, c) in visited:
                continue
            area += 1
            visited.add((r, c))
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc] == item:
                        if (nr, nc) not in visited:
                            queue.append((nr, nc))
                    else:
                        perimeter += 1
                else:
                    perimeter += 1

        cost += area * perimeter

print(cost)
