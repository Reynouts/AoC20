import aocutils
width = 0
height = 0
nbrs = {}


def get_neighbours(grid, position, nearsighted=False):
    global width
    global height
    global nbrs
    if position in nbrs:
        return nbrs[position]
    heading = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
    result = []
    for h in heading:
        cpos = position
        while True:
            cpos = tuple(map(sum, zip(cpos, h)))
            if cpos in grid:
                result.append(cpos)
                break
            elif cpos[0] >= width or cpos[1] >= height or cpos[0] < 0 or cpos[1] < 0:
                break # out of bounds
            if nearsighted:
                break # stop after direct neighbours
    nbrs[position] = result
    return result


def raycastr(grid, position, nearsighted=False):
    raycast = get_neighbours(grid, position, nearsighted)
    return sum([1 for ray in raycast if grid[ray] == "#"])


def cycle(grid, nearsighted, target):
    changes = {}
    for i in grid:
        if grid[i] == "L":
            if raycastr(grid, i, nearsighted) == 0:
                changes[i] = "#"
        elif grid[i] == "#":
            if raycastr(grid, i, nearsighted) >= target:
                changes[i] = "L"
    for i in changes:
        grid[i] = changes[i]
    return len(changes)


@aocutils.timeit
def solve(grid, nearsighted, target):
    global nbrs
    nbrs = {}
    result = 1
    while result > 0:
        result = cycle(grid, nearsighted, target)
    return list(grid.values()).count("#")


def main():
    global width
    global height

    with open('day11.txt', 'r') as f:
        data = f.readlines()
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c in ("#", "L"):
                grid[(x, y)] = c
    height = y+1
    width = x+1

    print(f"P1: {solve(grid.copy(), True, 4)}")
    print(f"P2: {solve(grid, False, 5)}")


if __name__ == "__main__":
    main()
