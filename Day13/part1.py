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
        int(input[i * 4 + 2].split(" ")[1].split("=")[1][:-1]),
        int(input[i * 4 + 2].split(" ")[2].split("=")[1]),
    )
    games.append((a, b, prize))

total_cost = 0


def valid_combinations(a, b, prize):
    a_x_max = prize[0] // a[0]
    a_y_max = prize[1] // a[1]
    b_x_max = prize[0] // b[0]
    b_y_max = prize[1] // b[1]
    a_max = min(a_x_max, a_y_max)
    b_max = min(b_x_max, b_y_max)
    valid_combinations = []
    for i in range(min(a_max, 100) + 1):
        for j in range(min(b_max, 100) + 1):
            if a[0] * i + b[0] * j == prize[0] and a[1] * i + b[1] * j == prize[1]:
                valid_combinations.append((i, j))
    return valid_combinations


def solve_game(game):
    a, b, prize = game
    cost = float("inf")
    combinations = valid_combinations(a, b, prize)
    if not combinations:
        return 0
    for combination in combinations:
        cost = min(cost, combination[0] * 3 + combination[1])
    return cost


for game in games:
    total_cost += solve_game(game)

print(total_cost)
