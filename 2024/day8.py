from enum import Enum


class Antenna:
    def __init__(self, symbol, pos):
        self.symbol = symbol
        self.pos = pos
    
    def __str__(self):
        return f"{self.symbol}: {self.pos}"


def print_matrix(matrix):
    for y in range(len(matrix)):
        print(*matrix[y])
    print("\n")


if __name__ == "__main__":
    with open("2024/temp/input8.txt") as f:
        matrix = list(f.read().splitlines())

    antennas = list()

    for y in range(len(matrix)):
        matrix[y] = list(matrix[y])
        for x in range(len(matrix)):
            if matrix[y][x] != ".":
                a = Antenna(matrix[y][x], (y, x))
                antennas.append(a)

    for a in antennas:
        print(a)

    print_matrix(matrix)
