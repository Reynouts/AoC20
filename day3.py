import aocutils as util
from functools import reduce


def solve(trees, dim, slopes):
    counts = []
    for slope in slopes:
        cnt = y = x = 0
        while y < dim[1]:
            x += slope[0]
            y += slope[1]
            if (x % (dim[0]), y) in trees:
                cnt += 1
        counts.append(cnt)
    return reduce(lambda i, j: i * j, counts)


def main():
    day = int(util.os.path.basename(__file__).split(".")[0].split("day")[1])
    data = util.get_file(day)

    trees = set()
    for y, line in enumerate(data):
        for x, element in enumerate(line):
            if element == "#":
                trees.add((x, y))
    dim = (x + 1, y + 1)

    slope = (3, 1)
    print("Part 1: {}".format(solve(trees, dim, [slope])))

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print("Part 2: {}".format(solve(trees, dim, slopes)))


if __name__ == "__main__":
    main()
