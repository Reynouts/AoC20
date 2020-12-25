from collections import defaultdict
import aocutils


def cycle(v, n=100):
    headings = ((2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1))
    for _ in range(n):
        _np = set()
        for i in v:
            bx = 0
            for h in headings:
                # check own bx value
                nb = (i[0] + h[0], i[1] + h[1])
                if nb in v:
                    bx += 1
                else:
                    # check neighbour (white)
                    bx2 = 0
                    for h2 in headings:
                        # check own bx value
                        nb2 = (nb[0] + h2[0], nb[1] + h2[1])
                        if nb2 in v:
                            bx2 += 1
                    if bx2 == 2:
                        # print("adding from white")
                        _np.add(nb)
            if bx == 1 or bx == 2:
                # print("adding from black")
                _np.add(i)
        v = _np
    return len(v)


def get_tiles(data):
    v = defaultdict(int)
    headings = {"e": (2, 0), "se": (1, 1), "sw": (-1, 1), "w": (-2, 0), "nw": (-1, -1), "ne": (1, -1)}
    for tile in data:
        current = (0, 0)
        prev = False
        for i, e in enumerate(tile.strip()):
            if prev:
                prev = False
                continue
            if i != len(tile.strip()) - 1:
                ins = tile[i:i + 2]
                if ins in headings:
                    e = ins
                    prev = True
            current = (current[0] + headings[e][0], current[1] + headings[e][1])
        v[current] = (v[current] + 1) % 2
    return v


@aocutils.timeit
def main():
    with open('day24.txt', 'r') as f:
        data = f.readlines()

    v = get_tiles(data)
    bxs = set([x for x in v if v[x] == 1])
    print("P1: {}".format(len(bxs)))
    print("P2: {}".format(cycle(bxs)))


if __name__ == "__main__":
    main()
