from collections import deque, defaultdict

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
        sides = defaultdict(list)
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
                        if (dr, dc) in [(0, 1), (0, -1)]:
                            sides[(c, (dr, dc))].append((r, c))
                        else:
                            sides[(r, (dr, dc))].append((r, c))
                else:
                    if (dr, dc) in [(0, 1), (0, -1)]:
                        sides[(c, (dr, dc))].append((r, c))
                    else:
                        sides[(r, (dr, dc))].append((r, c))

        total_sides = 0

        for side, pieces in sides.items():
            if len(pieces) == 1:
                total_sides += 1
                continue
            d = side[1]
            if d in [(0, 1), (0, -1)]:
                pieces = sorted(pieces, key=lambda x: x[0])
                groups = []
                for piece in pieces:
                    if not groups:
                        groups.append([piece])
                        continue
                    if piece[0] == groups[-1][-1][0] + 1:
                        groups[-1].append(piece)
                    else:
                        groups.append([piece])
                total_sides += len(groups)
            else:
                pieces = sorted(pieces, key=lambda x: x[1])
                groups = []
                for piece in pieces:
                    if not groups:
                        groups.append([piece])
                        continue
                    if piece[1] == groups[-1][-1][1] + 1:
                        groups[-1].append(piece)
                    else:
                        groups.append([piece])
                total_sides += len(groups)

        cost += area * total_sides

print(cost)
