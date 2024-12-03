import re

with open("2024/temp/input3.txt") as f:
    input_text = f.read()

corrected_memory = re.findall(r"mul\(\d+,\d+\)", input_text)
total_sum: int = 0

for equation in corrected_memory:
    numbers = re.findall(r"\d+", equation)
    multi = int(numbers[0]) * int((numbers[1]))
    total_sum += multi

print(f"Total Sum: {total_sum}")