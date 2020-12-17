import aocutils
from itertools import product


def get_neighbours(grid, position, r=4):
    heading = list(product([0, 1, -1], repeat=r))
    heading.remove((0, 0, 0, 0))
    cnt = 0
    for h in heading:
        cpos = tuple(map(sum, zip(position, h)))
        if cpos in grid:
            if grid[cpos] == 1:
                cnt += 1
    return cnt


def grow(grid, dimensions=4):
    cs = list(grid.keys())
    dim = []
    for i in range(dimensions):
        dim.append((min(cs, key=lambda x: x[i])[i], max(cs, key=lambda x: x[i])[i]))

    for w in range(dim[3][0] - 1, dim[3][1] + 2):
        for z in range(dim[2][0] - 1, dim[2][1] + 2):
            for y in range(dim[1][0] - 1, dim[1][1] + 2):
                for x in range(dim[0][0] - 1, dim[0][1] + 2):
                    if (x, y, z, w) not in grid.keys():
                        grid[(x, y, z, w)] = 0


def cycle(grid):
    changes = {}
    grow(grid)
    for pos in grid:
        n = get_neighbours(grid, pos)
        if grid[pos] == 1:
            if n == 2 or n == 3:
                changes[pos] = 1
            else:
                changes[pos] = 0
        elif grid[pos] == 0:
            if n == 3:
                changes[pos] = 1
    for pos in changes:
        grid[pos] = changes[pos]


def main():
    with open('day17.txt', 'r') as f:
        data = f.readlines()
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "#":
                grid[(x, y, 0, 0)] = 1
            elif c == ".":
                grid[(x, y, 0, 0)] = 0

    for n in range(6):
        cycle(grid)
    print(sum(grid.values()))


if __name__ == "__main__":
    main()
