import os
import time


def printg(grid):
    print("    ", end="")
    # for x in range(len(grid[0])):
    #    print(f"{x}", end=" ")
    print("\n", end="")
    for y in range(len(grid)):
        print(*grid[y])
    print("\n")


def bfs(start, grid):
    algo_grid = [["." for x in range(len(grid[0]))] for y in grid]
    algo_grid[start[0]][start[1]] = 0

    visited = list()
    queue = list()

    neighbours = find_next(start, visited, grid)
    visited.append(start)
    queue.extend(neighbours)

    trail_head_count = 0
    while queue:
        print(trail_head_count)
        new_pos = queue.pop(-1)
        y, x = new_pos
        algo_grid[y][x] = grid[y][x]
        printg(algo_grid)
        # time.sleep(0.1)
        os.system("clear")
        if grid[new_pos[0]][new_pos[1]] == 9:
            trail_head_count += 1
        visited.append(new_pos)
        neighbours = find_next(new_pos, visited, grid)
        queue.extend(neighbours)
    return trail_head_count


def find_next(pos: tuple, visited: list, grid: list):
    neighbours = list()
    y, x = pos
    greater_pos = grid[y][x] + 1
    # greater_pos = 1

    up, down = y - 1, y + 1
    left, right = x - 1, x + 1

    if up >= 0 and grid[up][x] == greater_pos and (up, x) not in visited:
        neighbours.append((up, x))

    if down < len(grid) and grid[down][x] == greater_pos and (down, x) not in visited:
        neighbours.append((down, x))

    if left >= 0 and grid[y][left] == greater_pos and (y, left) not in visited:
        neighbours.append((y, left))

    if right < len(grid[0]) and grid[y][right] == greater_pos and (y, right) not in visited:
        neighbours.append((y, right))

    return neighbours


def find_start(grid):
    start_pos = list()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                start_pos.append((y, x))
    return start_pos


with open("2024/temp/input10e.txt") as f:
    grid = [list(map(int, line.strip())) for line in f]

printg(grid)
start_pos = find_start(grid)

count = 0

for s in start_pos:
    t = bfs(s, grid)
    count += t

print("count: ", count)
