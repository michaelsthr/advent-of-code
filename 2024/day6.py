from enum import Enum
import os
import time


def print_matrix(matrix):
    for y in range(len(matrix)):
        print(*matrix[y])


def clear():
    os.system("clear")


class Mov(Enum):
    # (y,x)
    UP = -1, 0, "^"
    RIGHT = 0, 1, ">"
    DOWN = 1, 0, "v"
    LEFT = 0, -1, "<"


class Guard:
    def __init__(self, matrix):
        self.matrix = matrix

        self.mov = Mov.UP
        self.pos = self.find_pos()

        self.visit = [self.pos]
        self.visit_rot = [(self.pos, self.mov.name)]
        self.obstacles = []

    def predict_route(self) -> int:
        while True:
            print_matrix(self.matrix)
            print(f"POS: {self.pos}, MOV: {self.mov}\n")
            if self.check_end():
                # self.visited_no_dup = list(dict.fromkeys(self.visit))
                # self.loop_obstac_no_dup = list(dict.fromkeys(self.loop_obstac))
                return self.visit
            if self.check_obstacle("#"):
                self.rotate()
            # if self.check_loop(matrix):
            # self.loop_obstac.append(self.next_pos())
            # print(f"{self.next_pos()} is a possible loop location!")
            self.move()
            time.sleep(0.5)
            clear()

    def find_pos(self):
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if self.matrix[y][x] == "^":
                    return y, x

    def move(self):
        matrix[self.pos[0]][self.pos[1]] = "X"
        self.pos = self.next_pos()
        matrix[self.pos[0]][self.pos[1]] = self.mov.value[2]
        self.visit.append(self.pos)

    def rotate(self):
        if self.mov == Mov.UP:
            tmp = Mov.RIGHT
        if self.mov == Mov.RIGHT:
            tmp = Mov.DOWN
        if self.mov == Mov.DOWN:
            tmp = Mov.LEFT
        if self.mov == Mov.LEFT:
            tmp = Mov.UP
        self.mov = tmp

    def check_obstacle(self, obstacle):
        y, x = self.next_pos()
        if matrix[y][x] == obstacle:
            return True
        return False

    def check_end(self):
        y, x = self.next_pos()
        if x >= len(self.matrix[0]) or y >= len(self.matrix) or y == -1 or x == -1:
            return True
        return False

    def next_pos(self):
        return self.pos[0] + self.mov.value[0], self.pos[1] + self.mov.value[1]

    def check_loop(self):
        """Place obstacle in front and check if a loop is possible"""
        self.tmp_rot, self.tmp_pos = self.mov, self.pos
        c_matrix = matrix.copy()
        y, x = self.next_pos()
        s = list(c_matrix[y])
        s[x] = "O"
        c_matrix[y] = "".join(s)
        for i in c_matrix:
            print(i)
        print("")
        while self.check_end(c_matrix):
            if (self.pos, self.mov.name) in self.visited_and_rot:
                return True
            self.visited_and_rot.append((self.pos, self.mov.name))
            if not self.check_obstacle(c_matrix, "O"):
                self.rotate()
            self.move(c_matrix)
        self.mov, self.pos = self.tmp_rot, self.tmp_pos
        return False


if __name__ == "__main__":
    with open("2024/temp/input6e.txt") as f:
        matrix = f.read().splitlines()

    # matrix[y][x]
    for y in range(len(matrix)):
        matrix[y] = list(matrix[y])

    g = Guard(matrix)
    route = g.predict_route()
    len_route = len(list(dict.fromkeys(route)))
    print(f"Distinct positions: {len_route}")
    # print(f"Possible positions for obstacle loop {obstac_len}")
