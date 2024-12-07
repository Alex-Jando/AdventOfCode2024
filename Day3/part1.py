import re

with open("input.txt") as f:
    input_text = f.read()


def use_regex(input_text):
    return re.findall(r"mul\(\d+,\d+\)", input_text)


S = 0

for cmd in use_regex(input_text):
    a, b = map(int, cmd[4:-1].split(","))
    S += a * b

print(S)
