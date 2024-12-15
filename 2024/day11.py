import re
import functools

cache = {}


@functools.cache
def blink(stone, i):
    result = 0

    if i == 0:
        return 1

    if stone == 0:
        result += blink(1, i-1)
    elif len(str(stone)) % 2 == 0:
        tmp = str(stone)
        n = len(tmp) // 2
        left = tmp[:-n]
        right = tmp[-n:]
        result += blink(int(left), i-1) + blink(int(right), i-1)
    else:
        result += blink(stone * 2024, i-1)

    return result


if __name__ == "__main__":
    with open("2024/temp/input11.txt") as f:
        data = f.readline().strip()

    stones = re.findall(r"\d+", data)
    stones = [int(x) for x in stones]

    count = 0
    print("init count", count)
    for stone in stones:
        count += blink(stone, 75)

    print(f"They are {count} stones")
