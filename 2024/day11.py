import re


def blink(stones: list):
    new_stones = list()
    for i, stone in enumerate(stones):
        stone = stones[i]
        tmp = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(tmp) % 2 == 0:
            n = len(tmp) // 2
            left = tmp[:-n]
            right = tmp[-n:]
            new_stones.extend([int(left), int(right)])
        else:
            new_stones.append(stone * 2024)
    return new_stones


if __name__ == "__main__":
    with open("2024/temp/input11.txt") as f:
        data = f.readline().strip()

    stones = re.findall(r"\d+", data)
    stones = [int(x) for x in stones]

    for i in range(25):
        stones = blink(stones)
        # print(i, *stones)

    print(f"They are {len(stones)} stones")
