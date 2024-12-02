import re

with open("2024/temp/input2.txt") as f:
    input_text = f.readlines()

def check(line):
    is_increase = line[0] < line[1]

    for idx in range(len(line) - 1):
        is_large_difference = abs(line[idx] - line[idx + 1]) > 3
        is_equal = line[idx] == line[idx + 1]
        is_larger = line[idx] > line[idx + 1]
        
        if is_large_difference or is_equal or (is_increase and is_larger) or (not is_increase and not is_larger):
            return False

    return True
        
save: int = 0

for line in input_text:
    line = line.split(" ")
    line = [int(x) for x in line]

    if check(line) is True:
        save += 1

print("Save:", save)




