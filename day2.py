import aocutils as util


def main():
    day = int(util.os.path.basename(__file__).split(".")[0].split("day")[1])
    data = util.get_file(day)

    p1 = p2 = 0
    for l in data:
        bounds, letter, password = l.split(" ")
        bounds = list(map(int, bounds.split("-")))
        letter = letter[:-1]

        # part 1
        if bounds[0] <= password.count(letter) <= bounds[1]:
            p1 += 1

        # part 2
        if (password[bounds[0] - 1] == letter) ^ (password[bounds[1] - 1] == letter):
            p2 += 1

    print("Part 1: {}".format(p1))
    print("Part 2: {}".format(p2))


if __name__ == "__main__":
    main()
