with open("input.txt") as file:
    data = file.readlines()
equations = []

for line in data:
    val, nums = line.stript().split(":")
    equations.append((int(val), [int(num) for num in nums.split()]))

S = 0

for equation in equations:
    stack = [()]
    solvable = False
    while stack:
        cur_val = equation[1][0]
        operators = stack.pop()
        for i, operator in enumerate(operators):
            if operator == "+":
                cur_val += equation[1][i + 1]
            elif operator == "*":
                cur_val *= equation[1][i + 1]
        if len(operators) == len(equation[1]) - 1:
            if cur_val == equation[0]:
                solvable = True
                break
        else:
            stack.append(operators + ("+",))
            stack.append(operators + ("*",))
    if solvable:
        S += equation[0]

print(S)
