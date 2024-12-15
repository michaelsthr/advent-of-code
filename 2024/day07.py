import logging
import re
import time
from loguru import logger


def validate_equation_mul_plus(result, values, concat):
    solutions = list()
    solutions += [values[0]]
    i = 1

    while i < len(values):
        next_value = values[i]
        tmp_solutions = list()

        for solution in solutions:
            plus = solution + next_value
            mul = solution * next_value
            if concat:
                tmp_solutions += [int(str(solution) + str(next_value))]
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
    sums_with_concat = 0
    for equat in equation_lines:
        equat = equat.split(" ")
        result = int(re.findall(r"\d+", equat[0])[0])
        values = [int(x) for x in equat[1:]]
        a, b = False, False

        if validate_equation_mul_plus(result, values, concat=False):
            sums += result
            a = True

        if validate_equation_mul_plus(result, values, concat=True):
            sums_with_concat += result
            b = True

        if a is True:
            logger.success("")
            print("N-RESULT:", result, "VALUES:", values)
        if b is True:
            logger.success("")
            print("C-RESULT:", result, "VALUES:", values)
        if a is False and b is False:
            logger.error("")
            print("RESULT:", result, "VALUES:", values)

    print("sum:", sums)
    print("sum with concat:", sums_with_concat)
