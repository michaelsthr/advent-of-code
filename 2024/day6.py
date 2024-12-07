from enum import Enum


class Mov(Enum):
    # (y,x)
    UP = -1, 0
    RIGHT = 0, 1
    DOWN = 1, 0
    LEFT = 0, -1


class Player:
    def __init__(self):
        self.rot = Mov.UP
        self.pos = self.find_pos()
        self.visited = [self.pos]

    def predict_route(self) -> int:
        while True:
            if not self.check_end():
                self.visited_no_dup = list(dict.fromkeys(self.visited))
                return len(self.visited_no_dup)
            if not self.check_obstacle():
                self.rotate()
            self.move()

    def find_pos(self):
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[x][y] == "^":
                    return x, y

    def move(self):
        self.pos = self.pos[0] + self.rot.value[0], self.pos[1] + self.rot.value[1]
        self.visited.append(self.pos)

    def rotate(self):
        if self.rot == Mov.UP:
            tmp = Mov.RIGHT
        if self.rot == Mov.RIGHT:
            tmp = Mov.DOWN
        if self.rot == Mov.DOWN:
            tmp = Mov.LEFT
        if self.rot == Mov.LEFT:
            tmp = Mov.UP
        self.rot = tmp

    def check_obstacle(self):
        y, x = self.pos[0] + self.rot.value[0], self.pos[1] + self.rot.value[1]
        if matrix[y][x] == "#":
            return False
        return True

    def check_end(self):
        x, y = self.pos[0] + self.rot.value[0], self.pos[1] + self.rot.value[1]
        if x >= len(matrix[0]) or y >= len(matrix) or y == -1 or x == -1:
            return False
        return True


if __name__ == "__main__":
    with open("2024/temp/input6.txt") as f:
        matrix = f.read().splitlines()

    p = Player()
    pos_len = p.predict_route()
    print(f"Distinct positions: {pos_len}")
