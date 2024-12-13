with open("input.txt", "r") as file:
    input = file.readlines()

games = []

for i in range(len(input) // 4 + 1):
    a = (
        int(input[i * 4].split(" ")[2].split("+")[1][:-1]),
        int(input[i * 4].split(" ")[3].split("+")[1]),
    )
    b = (
        int(input[i * 4 + 1].split(" ")[2].split("+")[1][:-1]),
        int(input[i * 4 + 1].split(" ")[3].split("+")[1]),
    )
    prize = (
        int(input[i * 4 + 2].split(" ")[1].split("=")[1][:-1]) + 10000000000000,
        int(input[i * 4 + 2].split(" ")[2].split("=")[1]) + 10000000000000,
    )
    games.append((a, b, prize))

total_cost = 0


def diagonal_cost(a, b):
    diagonal = (float("inf"), 0, (0, 0))
    for i in range(700):
        for j in range(700):
            cost = i * 3 + j * 1
            dx = a[0] * i + b[0] * j
            dy = a[1] * i + b[1] * j
            if dx == dy:
                if dx == 0:
                    continue
                cost_per_unit = cost / dx
                if cost < diagonal[0] and cost_per_unit >= diagonal[1]:
                    diagonal = (cost, cost_per_unit, (i, j))
    if diagonal[0] == float("inf"):
        return diagonal
    return diagonal[2]


def valid_combinations(a, b, prize):
    a_x_max = prize[0] // a[0]
    a_y_max = prize[1] // a[1]
    b_x_max = prize[0] // b[0]
    b_y_max = prize[1] // b[1]
    a_max = min(a_x_max, a_y_max)
    b_max = min(b_x_max, b_y_max)
    valid_combinations = []

    for i in range(a_max + 1):
        for j in range(b_max + 1):
            if a[0] * i + b[0] * j == prize[0] and a[1] * i + b[1] * j == prize[1]:
                valid_combinations.append((i, j))
    return valid_combinations


def solve_game(game):
    a, b, prize = game
    cost = float("inf")
    diagonal = diagonal_cost(a, b)
    if diagonal[0] == float("inf"):
        return 0
    dx = a[0] * diagonal[0] + b[0] * diagonal[1]
    min_presses = (10000000000000 - 70000) // dx
    a_min = min_presses * diagonal[0]
    b_min = min_presses * diagonal[1]
    new_prize = (
        prize[0] - a[0] * a_min - b[0] * b_min,
        prize[1] - a[1] * a_min - b[1] * b_min,
    )
    combinations = valid_combinations(a, b, new_prize)
    if not combinations:
        return 0
    for combination in combinations:
        cost = min(cost, combination[0] * 3 + combination[1])
    cost += a_min * 3 + b_min
    return cost


for game in games:
    total_cost += solve_game(game)

print(total_cost)
