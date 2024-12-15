import re


def swap_until_true(order):
    print(order)
    for idx, num in enumerate(order):
        for r in rules:
            if num == r[0]:
                for x in range(0, idx - 1):
                    if r[1] == order[x]:
                        print(f"{r[1]} is sus")
                        l_idx = order.index(r[0])
                        r_idx = order.index(r[1])
                        order[l_idx], order[r_idx] = order[r_idx], order[l_idx]
                        print("swap", order[l_idx], order[r_idx])
                        return swap_until_true(order)
            if num == r[1]:
                for x in range(idx, len(order)):
                    if r[0] == order[x]:
                        print(f"{r[0]} is sus")
                        l_idx = order.index(r[0])
                        r_idx = order.index(r[1])
                        order[l_idx], order[r_idx] = order[r_idx], order[l_idx]
                        print("swap", order[l_idx], order[r_idx])
                        return swap_until_true(order)
    return order


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
swapped_sum = 0
for order in orders:
    if check_rules(order) is True:
        middle = int(len(order) / 2) + 1
        total_sum += int(order[middle - 1])
    else:
        norder = swap_until_true(order)
        middle = int(len(norder) / 2) + 1
        print(f"MIDDLE: {int(norder[middle - 1])}")
        swapped_sum += int(norder[middle - 1])

print("SUM:", total_sum)
print("SWAPPED SUM:", swapped_sum)
