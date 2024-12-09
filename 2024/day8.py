# find range between antennas pos
# --> map the anodes on each side

# difference between pos?


class Antenna:
    def __init__(self, symbol, vec):
        self.symbol = symbol
        self.vec = vec
        self.y = vec[0]
        self.x = vec[1]

    def __str__(self):
        return f"{self.symbol}: {self.vec} --> y:{self.y}, x:{self.x}"


def print_matrix(matrix):
    print("  ", end="")
    for x in range(len(matrix[0])):
        print(f"{x}", end=" ")
    print("\n", end="")
    for y in range(len(matrix)):
        print(y, *matrix[y])
    print("\n")


def add(v1: tuple, v2: tuple):
    return tuple(map(lambda i, j: i + j, v1, v2))


def sub(v1: tuple, v2: tuple):
    return tuple(map(lambda i, j: i - j, v1, v2))


if __name__ == "__main__":
    with open("2024/temp/input8e2.txt") as x:
        matrix = list(x.read().splitlines())

    antennas: list[Antenna] = list()

    for y in range(len(matrix)):
        matrix[y] = list(matrix[y])
        for x in range(len(matrix[y])):
            if matrix[y][x] != ".":
                a = Antenna(matrix[y][x], (y, x))
                antennas.append(a)
                print(a)

    for a in antennas:
        if a.symbol == "b":
            b = a
            print("b ant:", b)

    for a in antennas:
        if a.symbol != "b":
            y, x = add(a.vec, sub(a.vec, b.vec))
            print("vec", (y, x))
            matrix[y][x] = "#"

    # diff1 = abs(antennas[0].pos[0] - antennas[1].pos[0])
    # diff2 = abs(antennas[0].pos[1] - antennas[1].pos[1])

    # new_pos1 = antennas[1].pos[0] + diff1
    # new_pos2 = antennas[1].pos[1] + diff2

    # new_pos1b = antennas[0].pos[0] - diff1
    # new_pos2b = antennas[0].pos[1] - diff2

    # matriy[new_pos1][new_pos2] = "#"
    # matriy[new_pos1b][new_pos2b] = "#"

    # print((diff1, diff2))

    print_matrix(matrix)
