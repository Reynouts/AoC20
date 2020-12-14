from itertools import product


def create_mask(line, match="01"):
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


def main():
    with open('day14.txt', 'r') as f:
        data = f.readlines()

    patterns = ("10", "1X")
    masks = []
    memories = [{}, {}]
    for line in data:
        if "mask" in line:
            masks = []
            for i in patterns:
                masks.append(create_mask(line, i))
        else:
            mem, number = line.split(" = ")
            mem = int(mem.split("[")[1].split("]")[0])
            number = int(number)
            binr = ('{:036b}'.format(number), '{:036b}'.format(mem))
            for n, mask in enumerate(masks):
                nwm = ""
                for i, c in enumerate(binr[n]):
                    if i in mask:
                        c = mask[i]
                    nwm += c
                #p1
                if n == 0:
                    memories[n][mem] = int(nwm, 2)
                #p2
                else:
                    for c in combi(nwm):
                        memories[n][int(c, 2)] = number

    for i, memr in enumerate(memories):
        print("P{}: {}".format(i+1,sum([memr[x] for x in memr])))



if __name__ == "__main__":
    main()
