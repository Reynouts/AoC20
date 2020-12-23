from math import sqrt
import re
import numpy as np


class Tile:
    def __init__(self, ar):
        self.origin = ar
        self.backup = ar
        self.ar = ar
        self.top = ar[0]
        self.right = ar[:, -1]
        self.bottom = ar[-1]
        self.left = ar[:, 0]
        self.states = [self.reset, self.flipud, self.fliplr]
        self.cur = 0
        self.matches = [[], [], [], []]

    def next_state(self):
        self.cur += 1
        if self.cur == 3:
            self.cur = 0
        self.states[self.cur]()

    def addmatch(self, idx, id):
        self.matches[idx].append(id)

    def get_edges(self):
        return [self.top, self.right, self.bottom, self.left]

    def get_redges(self):
        return [self.top[::-1], self.right[::-1], self.bottom[::-1], self.left[::-1]]

    def flipud(self):
        self.ar = np.flipud(self.ar)
        self.backup = self.matches
        top, right, bottom, left = self.matches
        self.matches = [bottom, right, top, left]
        self.recalc()

    def fliplr(self):
        self.ar = np.fliplr(self.ar)
        self.backup = self.matches
        top, right, bottom, left = self.matches
        self.matches = [top, left, bottom, right]
        self.recalc()

    def rot90(self):
        self.ar = np.rot90(self.ar)
        self.backup = self.matches
        one, two, three, four = self.matches
        self.matches = [two, three, four, one]
        self.recalc()

    def rot180(self):
        self.backup = self.matches
        self.ar = np.rot90(self.ar)
        self.ar = np.rot90(self.ar)
        one, two, three, four = self.matches
        self.matches = [three, four, one, two]
        self.recalc()

    def reset(self):
        self.ar = self.origin
        self.matches = self.backup
        self.recalc()

    def recalc(self):
        self.top = self.ar[0]
        self.right = self.ar[:, -1]
        self.bottom = self.ar[-1]
        self.left = self.ar[:, 0]


def parse(data):
    tiles = {}
    for t in data:
        id, tile = t.split("\n", maxsplit=1)
        id = int(re.search(r'\d+', id).group())
        tile = np.asarray([list(l) for l in tile.strip().split("\n")])
        tiles[id] = Tile(tile)
    return tiles


def main():
    with open('day20.txt', 'r') as f:
        data = f.read().split("\n\n")
    tiles = parse(data)

    # top, right, bottom, left
    matches = {}
    for t1 in tiles:
        # top, right, bottom, left
        cnt = []
        for idx, e1 in enumerate(tiles[t1].get_edges()):
            edgecnt = 0
            for t2 in tiles:
                if t1 != t2:
                    for e2 in tiles[t2].get_edges() + tiles[t2].get_redges():
                        if (e1 == e2).all():
                            edgecnt += 1
                            tiles[t1].addmatch(idx, t2)
            cnt.append(edgecnt)
        matches[t1] = cnt
    p1 = 1
    corners = {}
    c = 0
    for m in matches:
        c += sum(matches[m])
        if sum(matches[m]) == 2:
            p1 *= m
            corners[m] = matches[m]
    print("P1: {}".format(p1))


    # take first corner
    topright = list(corners)[0]

    # rotate corner to have it right (doesn't have to flip, we flip others later)
    if corners[topright] == [0, 0, 1, 1]:
        tiles[topright].rot90()
    elif corners[topright] == [1, 0, 0, 1]:
        tiles[topright].rot180()
    elif corners[topright] == [1, 1, 0, 0]:
        tiles[topright].rot180()
        tiles[topright].rot90()

    dim = int(sqrt(len(tiles)))
    grid = [[-1 for i in range(dim)] for j in range(dim)]
    grid[0][0] = topright

    placed = set()
    placed.add(topright)
    for j in range(dim):
        for i in range(dim):
            if grid[i][j] != -1:
                # bottomleft
                if i == 0 and j == dim-1:
                    while tiles[grid[i][j]].matches[0] == [] or tiles[grid[i][j]].matches[0][0] != grid[i][j-1]:
                        tiles[grid[i][j]].rot90()
                    if not tiles[grid[i][j]].matches[1]:
                        tiles[grid[i][j]].fliplr()
                # leftmost column, not top
                elif i == 0 and j != 0:
                    while tiles[grid[i][j]].matches[3]:
                        tiles[grid[i][j]].rot90()
                    # if top does not match placed tile flipud
                    if tiles[grid[i][j]].matches[0] == [] or tiles[grid[i][j]].matches[0][0] != grid[i][j-1]:
                        tiles[grid[i][j]].flipud()
                # not leftmost
                if i != 0:
                    # while left placed tile does not match, rotate
                    while tiles[grid[i][j]].matches[3] == [] or tiles[grid[i][j]].matches[3][0] != grid[i-1][j]:
                        tiles[grid[i][j]].rot90()
                    if j != 0:
                        # if top does not match placed tile flipud
                        if tiles[grid[i][j]].matches[0] == [] or tiles[grid[i][j]].matches[0][0] != grid[i][j-1]:
                            tiles[grid[i][j]].flipud()
                    else:
                        # for top border
                        if tiles[grid[i][j]].matches[0]:
                            tiles[grid[i][j]].flipud()
                # place adjacent tiles
                if i != (dim-1):
                    grid[i+1][j] = tiles[grid[i][j]].matches[1][0]
                if i == 0 and j != (dim-1):
                    grid[i][j+1] = tiles[grid[i][j]].matches[2][0]

    #cut borders
    sgrid = []
    for j in range(dim):
        for x in range(1, 9):
            res = []
            for i in range(dim):
                res.extend(tiles[grid[i][j]].ar[x][1:-1])
            sgrid.append(res)
    img = np.array(sgrid)

    sm = ["                  # ","#    ##    ##    ###"," #  #  #  #  #  #   "]
    seamonster = []
    for j, l in enumerate(sm):
        for i, c in enumerate(l):
            if c == "#":
                seamonster.append((j, i))

    # find nesses in all orientations
    nessquares = []
    for i in [np.copy, np.flipud, np.fliplr]:
        img_ = i(img)
        for r in range(3):
            _img = np.rot90(img_, r)
            for j in range(len(_img)-len(sm)):
                for i in range(len(_img[0])-len(sm[1])):
                    valid = True
                    for item in seamonster:
                        y = j+item[0]
                        x = i+item[1]
                        if _img[y][x] != "#":
                            valid = False
                            break
                    if valid:
                        for item in seamonster:
                            y = j + item[0]
                            x = i + item[1]
                            nessquares.append((y, x))
    cnt = 0
    for j in img:
        for c in j:
            if c == "#":
                cnt += 1
    print("P2: {}".format(cnt - len(nessquares)))


if __name__ == "__main__":
    main()
