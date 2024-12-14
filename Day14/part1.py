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

robot_count = [0, 0, 0, 0]

for robot in robots:
    for _ in range(100):
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
    if robot[0][0] < MID_C and robot[0][1] < MID_R:
        robot_count[0] += 1
    elif robot[0][0] > MID_C and robot[0][1] < MID_R:
        robot_count[1] += 1
    elif robot[0][0] < MID_C and robot[0][1] > MID_R:
        robot_count[2] += 1
    elif robot[0][0] > MID_C and robot[0][1] > MID_R:
        robot_count[3] += 1

answer = robot_count[0] * robot_count[1] * robot_count[2] * robot_count[3]

print(answer)
