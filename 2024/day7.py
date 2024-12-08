import logging
import re
import time


def recursive(full_solution: list, sol: list, vals: list, i):
    print(i, sol)
    i += 1
    if i >= len(vals):
        # print("limit")
        return sol
    next_val = int(vals[i])
    # full_solution = full_solution
    # print(sol)
    tmp = []
    for s in sol:
        # print(s)
        plus = s + next_val
        mul = s * next_val

        tmp.append(plus)
        tmp.append(mul)
        # print("tmp", tmp)

    sol = tmp
    sol = tmp

    full_solution.append(plus)
    full_solution.append(mul)
    print("full_sos", full_solution)
    # print("sol", sol)

    return full_solution + recursive(
        full_solution=full_solution, sol=sol, vals=vals, i=i
    )


def check_eq(res, vals):
    full_solution = []
    sol = []
    sol.append(vals[0])
    print("FIRST SOL:", sol)
    solution = recursive(full_solution=full_solution, sol=sol, vals=vals, i=0)
    # print("solution:", solution)
    if res in solution:
        return True
    return False


with open("2024/temp/input7e.txt") as f:
    eqs = list(f.read().splitlines())

sums = 0
for eq in eqs:
    eq = eq.split(" ")
    result = re.findall(r"\d+", eq[0])
    vals = eq[1:]
    print("RES:", result, "VAL:", vals)
    vals = [int(x) for x in vals]
    result = [int(x) for x in result]
    if check_eq(result[0], vals):
        sums += result[0]
        print(result, "is true")
        continue
    print(result, "is false")

print("sum:", sums)
