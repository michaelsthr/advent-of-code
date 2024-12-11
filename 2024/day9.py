with open("2024/temp/input9.txt") as f:
    data = f.read().strip()

data = [int(x) for x in data]

blocks = []
free_space: bool = False

i = 0
for d in data:
    value = d
    for x in range(value):
        if free_space is True:
            blocks.append(".")
        else:
            blocks.append(i)
    if free_space is False:
        i += 1
    free_space = not free_space

last_idx = 0
for i, r in enumerate(reversed(blocks)):
    for j in range(last_idx, len(blocks)):
        if blocks[j] == ".":
            last_idx = j
            blocks[j] = r
            blocks[len(blocks) - i - 1] = "#"
            break

check_sum = 0
for i, val in enumerate(blocks):
    if val != "#":
        check_sum += i * val

# print(*blocks)
print("Checksum:", check_sum)
