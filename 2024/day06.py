from enum import Enum
import os
import time
import copy


def print_matrix(matrix):
    for y in range(len(matrix)):
        print(*matrix[y])

    # print("\n")


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
        self.obstac = []

    def predict_route(self) -> int:
        i = 0

        while True:
            # print_matrix(self.matrix)
            if self.check_end():
                return self.visit, self.obstac
            if self.check_obstacle("#"):
                self.rotate()
            if self.check_loop(i):
                self.obstac.append(self.next_pos())
            self.move("X")
            # time.sleep(0.4)
            # os.system("clear")
            i += 1
            # print(self.pos)
            print("FINSIHED:", i)

    def find_pos(self):
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if self.matrix[y][x] == "^":
                    return y, x

    def move(self, c):
        self.matrix[self.pos[0]][self.pos[1]] = c
        self.pos = self.next_pos()
        y, x = self.pos
        # print(self.pos)
        self.matrix[y][x] = self.mov.value[2]
        self.visit.append(self.pos)
        self.visit_rot.append((self.pos, self.mov.name))

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

    def check_obstacle(self, obstacle: str):
        y, x = self.next_pos()
        if self.matrix[y][x] == obstacle:
            return True
        return False

    def check_end(self):
        y, x = self.next_pos()
        if x >= len(self.matrix[0]) or y >= len(self.matrix) or y == -1 or x == -1:
            return True
        return False

    def next_pos(self):
        return self.pos[0] + self.mov.value[0], self.pos[1] + self.mov.value[1]

    def check_loop(self, i):
        """Place obstacle in front and check if a loop is possible"""
        tmp_mov = self.mov
        tmp_pos = self.pos
        tmp_matrix = copy.deepcopy(self.matrix)
        tmp_visit = copy.copy(self.visit)
        tmp_visit_rot = copy.copy(self.visit_rot)

        y, x = self.next_pos()
        if (y, x) in tmp_visit:
            return False
        else:
            self.matrix[y][x] = "#"

        loop = list()
        while not self.check_end():
            # print("loop", i, self.pos)
            if self.check_obstacle("#"):
                self.rotate()
                continue
                # faster move func
            self.move("r")

            self.visit.append(self.pos)
            self.visit_rot.append((self.pos, self.mov.name))
            # print(self.loop)
            # print((self.pos, self.mov.name))

            if (self.pos, self.mov.name) in tmp_visit_rot:
                self.visit = tmp_visit
                self.visit_rot = tmp_visit_rot
                self.matrix = tmp_matrix
                self.pos = tmp_pos
                self.mov = tmp_mov
                # print("true")
                return True
            if (self.pos, self.mov.name) in loop:
                self.visit = tmp_visit
                self.visit_rot = tmp_visit_rot
                self.matrix = tmp_matrix
                self.pos = tmp_pos
                self.mov = tmp_mov
                # print("true")
                return True
            loop.append((self.pos, self.mov.name))
            # print_matrix(self.matrix)
            # time.sleep(1)
            # os.system("clear")
            # print("end")

        self.visit = tmp_visit
        self.visit_rot = tmp_visit_rot
        self.matrix = tmp_matrix
        self.pos = tmp_pos
        self.mov = tmp_mov

        return False


if __name__ == "__main__":
    with open("2024/temp/input6.txt") as f:
        matrix = f.read().splitlines()

    # matrix[y][x]
    for y in range(len(matrix)):
        matrix[y] = list(matrix[y])

    g = Guard(matrix)
    route, obstac = g.predict_route()
    len_route = len(list(dict.fromkeys(route)))
    len_obstac = len(list(dict.fromkeys(obstac)))
    print(f"Distinct positions: {len_route}")
    print(f"Possible positions for obstacle loop {len_obstac}")
