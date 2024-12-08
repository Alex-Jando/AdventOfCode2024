from collections import defaultdict
from itertools import permutations

with open("input.txt", "r") as file:
    data = file.readlines()

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
            i = 1
            while True:
                newNode = (
                    (otherAnttena[0] - startAnttena[0]) * i + startAnttena[0],
                    (otherAnttena[1] - startAnttena[1]) * i + startAnttena[1],
                )
                if (
                    newNode[0] < 0
                    or newNode[0] >= R
                    or newNode[1] < 0
                    or newNode[1] >= C
                ):
                    break
                antiNodes.add(newNode)
                i += 1

print(len(antiNodes))
