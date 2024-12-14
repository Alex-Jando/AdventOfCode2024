with open("input.txt") as f:
    data = f.read().split("\n")

robots = [
    [
        list(map(int, i.split(" ")[0].split("=")[1].split(","))),
        list(map(int, i.split(" ")[1].split("=")[1].split(","))),
    ]
    for i in data
]

R = 103
C = 101

MID_R = R // 2
MID_C = C // 2

common_locations = set()

robot_count = [0, 0, 0, 0]


def displayFormation(robots):
    grid = [["." for _ in range(C)] for _ in range(R)]
    for robot in robots:
        grid[robot[0][1]][robot[0][0]] = "#"
    return "\n".join(["".join(row) for row in grid])


for i in range(100000):
    for robot in robots:
        nc = robot[0][0] + robot[1][0]
        nr = robot[0][1] + robot[1][1]
        if nc < 0:
            nc += C
        if nr < 0:
            nr += R
        if nc >= C:
            nc -= C
        if nr >= R:
            nr -= R
        robot[0] = [nc, nr]
    if "#########" in (display := displayFormation(robots)):
        print(display)
        print("Found at time:", i + 1, "seconds")
        input("Press Enter to continue...")
