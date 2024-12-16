import os
import time
import copy


def printg(grid):
    for y in grid:
        print(*y)


def calc_perimeter(plants: list) -> int:
    count = 0
    for plant in plants:
        y, x = plant
        neightbours = [(y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)]
        for neightbour in neightbours:
            if neightbour not in plants:
                count += 1
    return count


def dfs(plant: str, start: tuple, grid: list) -> list:
    vis_grid = [["." for x in range(len(grid[0]))] for y in grid]
    vis_grid[start[0]][start[1]] = plant

    not_cache = []

    def find_next_pos(pos: tuple) -> list:
        next_pos = []
        y, x = pos
        next_posis = [(y - 1, x), (y + 1, x), (y, x + 1), (y, x - 1)]
        for posi in next_posis:
            if posi not in not_cache:
                y, x = posi
                in_bound = y >= 0 and x >= 0 and y < len(
                    grid) and x < len(grid[0])
                if posi not in visited and in_bound and plant == grid[y][x]:
                    next_pos.append(posi)
                not_cache.append(posi)

        return next_pos

    visited: list = [start]
    queue: list = find_next_pos(start)

    while queue:
        next_pos = queue.pop(-1)
        y, x = next_pos

        vis_grid[y][x] = grid[y][x]
        # printg(vis_grid)

        # time.sleep(0.2)
        # os.system("clear")

        visited.append(next_pos)
        queue.extend(find_next_pos(next_pos))

    return visited


if __name__ == "__main__":
    with open("2024/temp/input12.txt") as f:
        grid = [list(line.strip()) for line in f]

    plants = {}
    price = 0
    i = 0
    visited = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            plant = grid[y][x]
            if plant not in plants:
                plants[plant] = dfs(plant, (y, x), grid)
                visited.extend(plants[plant])
            if (y, x) not in plants[plant] and (y, x) not in visited:
                plants[plant + str(i)] = dfs(plant, (y, x), grid)
                visited.extend(plants[plant + str(i)])
                i += 1

    price = 0
    for plant in plants:
        area = len(plants[plant])
        perimeter = calc_perimeter(plants[plant])
        result = area * perimeter
        price += result
        print(f"plant: {plant}: {area} + {perimeter} = {result}")

    print(f"price: {price}")
