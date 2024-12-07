from collections import defaultdict

rules = defaultdict(list)
updates = []

with open("input.txt") as f:
    data = f.readlines()

on_rules = True

for line in data:
    if line == "\n":
        on_rules = False
        continue
    if on_rules:
        line = line.strip()
        key, value = map(int, line.split("|"))
        rules[key].append(value)
    else:
        updates.append([int(i) for i in line.strip().split(",")])

correct_updates = []

for update in updates:
    correct = True
    for i in range(len(update)):
        if not correct:
            break
        for j in range(len(update)):
            if not correct:
                break
            for rule in rules.get(update[i], []):
                if rule == update[j]:
                    if i > j:
                        correct = False
                        break
    if correct:
        correct_updates.append(update)

middle_sum = 0

for update in correct_updates:
    middle_sum += update[len(update) // 2]

print(middle_sum)
