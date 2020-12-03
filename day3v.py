import aocutils as util
from functools import reduce
import time
import os

v = 1


def draw_start(level):
    global v
    v = 1
    with open('start.txt', 'r') as f:
        tobo = f.read()
    cls()
    start = "\n       --- Toboggan Trajectory Simulator ---      \n"
    levels = ["       --- head out for your first slide ---      \n\n",
              "       --- congrats making it out alive! ---      \n\n"]
    start += levels[min(level, len(levels)-1)]
    start += "\033[33m" + tobo + "\033[0m\n\n"
    start += "       --- Loading level " + str(level)
    for i in range(13):
        print(start)
        start += "."
        time.sleep(0.2)
        cls()
    start += " ---      \n"
    start += "                   --- LET'S GO ---      "
    print(start)
    time.sleep(1)


def draw(current, trees, dim, viewport, visited, tree_count, slope):
    global v
    vmax = 0.050
    result = "\n      --- Toboggan Trajectory Simulator ---      \n"

    hitclr = "\033[0m"
    cend = "\033[0m"

    shift_x = shift_y = 0
    frame_x = (viewport[0] / 2) + slope[0] * 3
    frame_y = (viewport[1] / 2) + slope[1] * 3

    if current[0] > frame_x:
        shift_x = current[0] - frame_x
    if current[1] > frame_y:
        shift_y = current[1] - frame_y

    for j in range(viewport[1]):
        for i in range(viewport[0]):
            sq_x = i + shift_x
            sq_y = j + shift_y
            if (sq_x, sq_y) in visited:
                color = '\033[92m'
            else:
                color = cend
            if (sq_x, sq_y) == current:
                if (sq_x % dim[0], sq_y) in trees:
                    hitclr = '\033[41m'
                    result += hitclr
                result += '\033[93m' + u"\u0565" + cend
            elif (sq_x % dim[0], sq_y) in trees:
                result += color + "#" + cend
            elif sq_y < dim[1]:
                result += color + "." + cend
            else:
                result += " "
        result += "\n"
    result += "Tree count: {}{}{}\n".format(hitclr, tree_count, cend)
    time.sleep(v)
    cls()
    print(result)
    v = max(v * 0.88, vmax)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def solve(trees, dim, slopes):
    counts = []
    for slope in slopes:
        draw_start(len(counts))
        visited = set()
        cnt = y = x = 0
        while y < dim[1]:
            visited.add((x, y))
            draw((x, y), trees, dim, (50, 20), visited, cnt, slope)
            x += slope[0]
            y += slope[1]
            if (x % (dim[0]), y) in trees:
                cnt += 1
        counts.append(cnt)
    return reduce(lambda i, j: i * j, counts)


def main():
    day = int(util.os.path.basename(__file__).split(".")[0].split("day")[1][:-1])
    data = util.get_file(day)

    trees = set()
    for y, line in enumerate(data):
        for x, element in enumerate(line):
            if element == "#":
                trees.add((x, y))
    dim = (x + 1, y + 1)

    slope = (3, 1)
    # print("Part 1: {}".format(solve(trees, dim, [slope])))

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print("Part 2: {}".format(solve(trees, dim, slopes)))


if __name__ == "__main__":
    main()
