from collections import defaultdict

with open("input.txt") as f:
    stones = [int(num) for num in f.read().strip().split()]

stone_counts = defaultdict(int)

for stone in stones:
    stone_counts[stone] += 1

memo = {0: [1]}


def blink(stone):
    if stone in memo:
        return memo[stone]
    stone_str = str(stone)
    length = len(stone_str)
    if length % 2 == 0:
        memo[stone] = [int(stone_str[: length // 2]), int(stone_str[length // 2 :])]
        return [int(stone_str[: length // 2]), int(stone_str[length // 2 :])]
    else:
        memo[stone] = [2024 * stone]
        return [2024 * stone]


for _ in range(75):
    new_counts = defaultdict(int)
    for stone, count in stone_counts.items():
        for new_stone in blink(stone):
            new_counts[new_stone] += count
    stone_counts = new_counts

print(sum(stone_counts.values()))
