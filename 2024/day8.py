# find range between antennas pos
# --> map the anodes on each side

# difference between pos?
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


def add(v1: tuple, v2: tuple):
    return tuple(map(lambda i, j: i + j, v1, v2))


def sub(v1: tuple, v2: tuple):
    return tuple(map(lambda i, j: i - j, v1, v2))


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

    for antenna in grouped_antennas:
        for i, a in enumerate(antenna):
            tmp_antennas = copy.deepcopy(antenna)
            tmp_antennas.pop(i)
            for b in tmp_antennas:
                y, x = add(b.vec, sub(b.vec, a.vec))
                # print(f"{a.symbol}: {(y, x)} = add({b.vec}, sub({b.vec}, {a.vec}))")
                if y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0]):
                    # print("add antinode", (y, x))
                    unique_loc.append((y, x))
                    grid[y][x] = "#"
                # else:
                # print("skip antinode:", (y, x))

    sum_unique_loc = len(set(unique_loc))
    print_grid(grid)
    print("Unique locations containing antinodes:", sum_unique_loc)
