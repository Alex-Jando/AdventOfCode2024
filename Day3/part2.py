import re

with open("input.txt") as f:
    input_text = f.read()


def use_regex(input_text):
    return re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_text)


S = 0
ENABLED = True

for cmd in use_regex(input_text):
    if cmd == "do()":
        ENABLED = True
    elif cmd == "don't()":
        ENABLED = False
    else:
        if ENABLED:
            a, b = map(int, cmd[4:-1].split(","))
            S += a * b

print(S)
