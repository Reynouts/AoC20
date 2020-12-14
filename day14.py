from itertools import product
import re


def create_mask(line, match):
    mask = {}
    bitmask = line.split("=")[1].strip()
    for i, c in enumerate(bitmask):
        if c in match:
            mask[i] = c
    return mask


def combi(b):
    n = b.count("X")
    results = []
    for p in product([0,1], repeat=n):
        res = ""
        cnt = 0
        for c in b:
            if c != "X":
                res += c
            else:
                res += str(p[cnt])
                cnt += 1
        results.append(res)
    return results


def solve(data, mode):
    pattern = ("10", "X1")
    mask = []
    memory = {}
    for line in data:
        if "mask" in line:
            mask = create_mask(line, pattern[mode-1])
        else:
            nm = [int(s) for s in re.findall(r'\d+', line)]
            binr = '{:036b}'.format(nm[mode-1])
            nwm = ""
            for i, c in enumerate(binr):
                if i in mask:
                    c = mask[i]
                nwm += c
            if mode == 1:
                memory[nm[1]] = int(nwm, 2)
            if mode == 2:
                for c in combi(nwm):
                    memory[int(c, 2)] = nm[0]
    return sum([memory[x] for x in memory])


def main():
    with open('day14.txt', 'r') as f:
        data = f.readlines()
    print("P1: {}".format(solve(data, 1)))
    print("P2: {}".format(solve(data, 2)))


if __name__ == "__main__":
    main()
