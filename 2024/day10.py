import os


def main():
    with open("2024/temp/input10.txt") as f:
        grid = [list(map(int, line.strip())) for line in f]

    count = 0
    for s in find_start(grid):
        t = bfs(s, grid)
        count += t

    print("count: ", count)


def find_start(grid):
    start_pos = list()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                start_pos.append((y, x))
    return start_pos


def bfs(start, grid):
    visualisation_grid = [["." for x in range(len(grid[0]))] for y in grid]
    visualisation_grid[start[0]][start[1]] = 0

    visited = [start]
    queue = find_next(start, visited, grid)
    count = 0

    while queue:
        print(count)
        next_pos = queue.pop(-1)
        y, x = next_pos
        visualisation_grid[y][x] = grid[y][x]

        for i in range(len(visualisation_grid)):
            print(*visualisation_grid[i])

        # time.sleep(0.1)
        os.system("clear")

        if grid[y][x] == 9:
            count += 1

        #################################################
        # visited.append(next_pos)  # Add for part 1 :) #
        #################################################

        queue.extend(find_next(next_pos, visited, grid))
    return count


def find_next(pos: tuple, visited: list, grid: list):
    neighbours = list()
    y, x = pos
    greater_pos = grid[y][x] + 1

    up, down = y - 1, y + 1
    left, right = x - 1, x + 1

    # Validate every next position
    if up >= 0 and grid[up][x] == greater_pos and (up, x) not in visited:
        neighbours.append((up, x))

    if down < len(grid) and grid[down][x] == greater_pos and (down, x) not in visited:
        neighbours.append((down, x))

    if left >= 0 and grid[y][left] == greater_pos and (y, left) not in visited:
        neighbours.append((y, left))

    if (
        right < len(grid[0])
        and grid[y][right] == greater_pos
        and (y, right) not in visited
    ):
        neighbours.append((y, right))

    return neighbours


if __name__ == "__main__":
    main()
