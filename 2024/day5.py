import re


def check_rules(order):
    for idx, num in enumerate(order):
        for r in rules:
            if num == r[0]:
                for x in range(0, idx - 1):
                    if r[1] == order[x]:
                        return False
            if num == r[1]:
                for x in range(idx, len(order)):
                    if r[0] == order[x]:
                        return False
    return True


with open("2024/temp/input5.txt") as f:
    lines = f.read().splitlines()

rules = []
orders = []

for line in lines:
    if line == "":
        continue
    numbers = re.findall(r"\d+", line)
    if "|" in line:
        rules.append(numbers)
    else:
        orders.append(numbers)

total_sum = 0
for order in orders:
    if check_rules(order) is True:
        middle = int(len(order) / 2) + 1
        total_sum += int(order[middle - 1])

print("SUM:", total_sum)
