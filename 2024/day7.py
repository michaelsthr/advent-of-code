import logging
import re
import time
from loguru import logger


def validate_equation(result, values):
    solutions = list()
    solutions += [values[0]]
    i = 1

    while i < len(values):
        next_value = values[i]
        tmp_solutions = list()

        for solution in solutions:
            plus = solution + next_value
            mul = solution * next_value
            tmp_solutions += [plus, mul]
            
        solutions = tmp_solutions
        i += 1

    if result in solutions:
        return True
    return False


if __name__ == "__main__":
    with open("2024/temp/input7.txt") as f:
        equation_lines = list(f.read().splitlines())

    sums = 0
    for equat in equation_lines:
        equat = equat.split(" ")
        result = int(re.findall(r"\d+", equat[0])[0])
        values = [int(x) for x in equat[1:]]

        if validate_equation(result, values):
            sums += result
            logger.success("")
            print("RESULT:", result, "VALUES:", values)
            continue

        logger.error("")
        print("RESULT:", result, "VALUES:", values)

    print("sum:", sums)
