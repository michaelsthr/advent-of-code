def main():
    with open("2024/temp/input9.txt") as f:
        data = f.read().strip()

    """
    defrac1 --> Part1
    defrac2 --> Part2
    """

    data = [int(x) for x in data]
    blocks = defrac2(data)

    res = []
    for b in blocks:
        for i in b:
            res.append(i)

    check_sum = 0
    for i, val in enumerate(res):
        if val != ".":
            check_sum += i * val

    print("Checksum:", check_sum)


def sort_blocks_list(data):
    blocks = []
    free_space: bool = False
    i = 0
    for d in data:
        value = d
        block = []
        for x in range(value):
            if free_space is True:
                block.append(".")
            else:
                block.append(i)
        if len(block) != 0:
            blocks.append(block)
        if free_space is False:
            i += 1
        free_space = not free_space
    return blocks


def sort_blocks(data):
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
    return blocks


def print_b(blocks):
    print("blocks: ", end="")
    for b in blocks:
        print(*b, end=" ")


def defrac2(data):
    blocks = sort_blocks_list(data)
    for l, bl in enumerate(blocks):
        print(f"...{l}...")
        if bl[0] == ".":
            for r, br in enumerate(reversed(blocks)):
                if br[0] == ".":
                    continue
                if l > len(blocks) - 1 - r:
                    break
                if len(bl) >= len(br):
                    diff = len(bl) - len(br)
                    # swap
                    tmp = ["."] * len(br)
                    blocks[l] = blocks[len(blocks) - 1 - r]
                    blocks[len(blocks) - 1 - r] = tmp
                    # insert difference
                    space = ["."] * diff
                    if len(space) >= 1:
                        blocks.insert(l + 1, space)
                    break
                else:
                    continue
    return blocks


def defrac1(blocks):
    blocks = sort_blocks(blocks)
    last_idx = 0
    for i, r in enumerate(reversed(blocks)):
        for j in range(last_idx, len(blocks)):
            if blocks[j] == ".":
                last_idx = j
                blocks[j] = r
                blocks[len(blocks) - i - 1] = "#"
                break
    return blocks


if __name__ == "__main__":
    main()