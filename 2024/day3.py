import re


def multiply_p1(memory):
    total_sum = 0
    for equation in memory:
        numbers = re.findall(r"\d+", equation)
        multi = int(numbers[0]) * int((numbers[1]))
        total_sum += multi
    return total_sum

def multiply_p2(memory):
    total_sum = 0
    do: bool = True
    for item in memory:
        if item == "do()": do = True
        if item == "don't()": do = False
        if do is True and item != "do()":
            numbers = re.findall(r"\d+", item)
            multi = int(numbers[0]) * int((numbers[1]))
            total_sum += multi
    return total_sum

with open("2024/temp/input3.txt") as f:
    input_text = f.read()

corrected_memory_p1 = re.findall(r"mul\(\d+,\d+\)", input_text)
corrected_memory_p2 = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_text)

total_sum_p1 = multiply_p1(corrected_memory_p1)
total_sum_p2 = multiply_p2(corrected_memory_p2)

print(f"Total Sum1: {total_sum_p1}")
print(f"Total Sum2: {total_sum_p2}")
