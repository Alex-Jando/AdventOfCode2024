from collections import defaultdict
from itertools import permutations

with open("input.txt", "r") as file:
    data = file.readlines()

# data = [
#     "..........",
#     "..........",
#     "..........",
#     "....a.....",
#     "..........",
#     ".....a....",
#     "..........",
#     "..........",
#     "..........",
#     "..........",
# ]

grid = [[c for c in line.strip()] for line in data]

R = len(grid)
C = len(grid[0])

attenaLocation = defaultdict(list)

for row in range(R):
    for col in range(C):
        if grid[row][col] == ".":
            continue
        attenaLocation[grid[row][col]].append((row, col))

antiNodes = set()

for locations in attenaLocation.values():
    for anttenas in permutations(locations):
        startAnttena, *otherAntenas = anttenas
        for otherAnttena in otherAntenas:
            newNode = (
                (otherAnttena[0] - startAnttena[0]) * 2 + startAnttena[0],
                (otherAnttena[1] - startAnttena[1]) * 2 + startAnttena[1],
            )
            if newNode[0] < 0 or newNode[0] >= R or newNode[1] < 0 or newNode[1] >= C:
                continue
            antiNodes.add(newNode)

print(len(antiNodes))
