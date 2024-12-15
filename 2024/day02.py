with open("2024/temp/input2.txt") as f:
    input_text = f.readlines()

def check(line):
    is_increase = line[0] < line[1]

    for idx in range(len(line) - 1):
        is_large_difference = abs(line[idx] - line[idx + 1]) > 3
        is_equal = line[idx] == line[idx + 1]
        is_next_larger = line[idx] < line[idx + 1]

        if (
            is_large_difference or is_equal
            or (is_increase and not is_next_larger)
            or (not is_increase and is_next_larger)
        ):
            return False, idx

    return True, _

strict_save: int = 0
tolerate_save: int = 0

for line in input_text:
    line = line.split(" ")
    line = [int(x) for x in line]

    result, idx = check(line)
    if result is True:
        strict_save += 1
    else:
        l1 = line.copy()
        l2 = line.copy()
        l3 = line.copy()

        # Some edge cases
        l2.pop(idx)
        l1.pop(0)
        l3.pop(idx + 1)

        for line in [l1, l2, l3]:
            result, _ = check(line)
            if result is True:
                tolerate_save += 1
                break

print(f"Strict Save: {strict_save}")
print(f"Tolerate Save: {strict_save + tolerate_save}")
