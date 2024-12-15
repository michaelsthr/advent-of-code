import copy


class Antenna:
    def __init__(self, symbol, vec):
        self.symbol = symbol
        self.vec = vec
        self.y = vec[0]
        self.x = vec[1]

    def __str__(self):
        return f"{self.symbol}: {self.vec} --> y:{self.y}, x:{self.x}"


def print_grid(grid):
    print("  ", end="")
    for x in range(len(grid[0])):
        print(f"{x}", end=" ")
    print("\n", end="")
    for y in range(len(grid)):
        print(y, *grid[y])
    print("\n")


def add(v1: tuple, v2: tuple) -> tuple:
    return tuple(map(lambda i, j: i + j, v1, v2))


def sub(v1: tuple, v2: tuple) -> tuple:
    return tuple(map(lambda i, j: i - j, v1, v2))


def mul(n: int, v: tuple) -> tuple:
    y = n * v[0]
    x = n * v[1]
    # print(f"{y, x} = {n} * {v[0]} and {n} * {v[1]}")
    return (n * v[0], n * v[1])


if __name__ == "__main__":
    with open("2024/temp/input8.txt") as x:
        grid = list(x.read().splitlines())

    antennas: list[Antenna] = list()
    symbols = set()

    for y in range(len(grid)):
        grid[y] = list(grid[y])
        for x in range(len(grid[y])):
            if grid[y][x] != ".":
                a = Antenna(grid[y][x], (y, x))
                antennas.append(a)
                symbols.add(a.symbol)
                print(a)

    # [a, c, v, a, c, a, c, k] --> [[a,a,a],[c,c,c],[v],[k]]
    grouped_antennas = list()
    for s in symbols:
        tmp = []
        for a in antennas:
            if s == a.symbol:
                tmp.append(a)
        if len(tmp) != 0:
            grouped_antennas.append(tmp)

    unique_loc = list()
    unique_loc2 = list()

    for antenna in grouped_antennas:
        for i, a in enumerate(antenna):
            j, l = a.vec
            # grid[j][l] = "#"
            unique_loc2.append(a.vec)
            tmp_antennas = copy.deepcopy(antenna)
            tmp_antennas.pop(i)
            for b in tmp_antennas:
                c = sub(b.vec, a.vec)
                y, x = add(b.vec, c)
                vec = (y, x)
                # print(f"{a.symbol}: {(y, x)} = add({b.vec}, sub({b.vec}, {a.vec}))")
                if y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0]):
                    # print("add antinode", (y, x))
                    unique_loc.append((y, x))
                    grid[y][x] = "#"
                    # go up
                    new_vec = copy.deepcopy(vec)
                    ik = 1
                    while True:
                        print(f"il = {ik}")
                        y, x = add(b.vec, mul(ik, c))
                        # print(mul(ik, new_vec), "+", b.vec, "=", (y, x))
                        if y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0]):
                            unique_loc2.append((y, x))
                            grid[y][x] = "#"
                            ik += 1
                        else:
                            print("skip", (y, x))
                            break
                    # go down
                    new_vec = copy.deepcopy(vec)
                    il = -1
                    while True:
                        print(f"il = {il}")
                        y, x = add(b.vec, mul(il, c))
                        # print(mul(il, new_vec), "+", b.vec, "=", (y, x))
                        if y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0]):
                            unique_loc2.append((y, x))
                            grid[y][x] = "#"
                            il -= 1
                        else:
                            print("skip", (y, x))
                            break
            print_grid(grid)

            # else:
            # print("skip antinode:", (y, x))

    alle = unique_loc + unique_loc2
    sum_unique_loc = len(set(unique_loc))
    sum_unique_loc2 = len(set(alle))
    print("Unique locations containing antinodes:", sum_unique_loc)
    print("Unique locations containing antinodes (part 2):", sum_unique_loc2)
