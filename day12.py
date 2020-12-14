def move(v, ship, wp):
    mv = tuple(v * e for e in wp)
    return tuple(map(sum, zip(ship, mv)))


def rwp(wp, v):
    x, y = wp
    v %= 360
    if v == 90:
        return y, x * -1
    elif v == 180:
        return x * -1, y * -1
    elif v == 270:
        return y * -1, x
    else:
        return x, y


def cycle(data, actor, waypoint):
    acts = {
        "E": lambda x, p: (p[0] + x, p[1]),
        "W": lambda x, p: (p[0] - x, p[1]),
        "S": lambda x, p: (p[0], p[1] - x),
        "N": lambda x, p: (p[0], p[1] + x),
    }

    mvrs = [(0,0), waypoint] # ship and wp
    for line in data:
        i = line[0]
        v = int(line[1:])
        if i == "F":
            mvrs[0] = move(v, *mvrs)
        elif i in "RL":
            if i == "L":
                v = v * -1
            mvrs[1] = rwp(mvrs[1], v)
        else:
            mvrs[actor] = acts[i](v, mvrs[actor])
    return abs(mvrs[0][0]) + abs(mvrs[0][1])


def main():
    with open('day12.txt', 'r') as f:
        data = f.readlines()
    print(f"P1: {cycle(data, 0, (1, 0))}")
    print(f"P2: {cycle(data, 1, (10, 1))}")


if __name__ == "__main__":
    main()
