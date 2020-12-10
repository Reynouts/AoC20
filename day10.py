from collections import defaultdict
import functools


def skive_old(mem, ads, jolt=0, idx=0):
    if mem[idx][jolt] != -1:
        # Already know how many paths from here
        return mem[idx][jolt]
    if ads[idx]-jolt <= 3:
        # A possible adapter!
        if idx == len(ads) - 1:
            # The end adapter!
            mem[idx][jolt] = 1
        else:
            # Calculate amount of paths. Continue with current jolt and split path with jolt of current adapter
            mem[idx][jolt] = skive_old(mem, ads, jolt, idx + 1) + skive_old(mem, ads, ads[idx], idx + 1)
    else:
        # this adapter does not fit, ending path.
        mem[idx][jolt] = 0
    # return amount of paths from this point, given the start jolt
    return mem[idx][jolt]


def main():
    with open('day10.txt', 'r') as f:
        ads = sorted(list(map(int, f.readlines())))

    n = {1: 0, 2: 0, 3: 0}
    j = 0
    for t in ads:
        if t - j <= 3:
            n[t - j] += 1
            j = t
    print("P1: {}".format(n[1] * (n[3]+1)))

    @functools.lru_cache(maxsize=None)
    def skive(jolt=0, idx=0):
        if ads[idx] - jolt <= 3:
            if idx == len(ads) - 1:
                return 1
            else:
                return skive(jolt, idx + 1) + skive(ads[idx], idx + 1)
        else:
            return 0

    print("P2: {}".format(skive()))

    memory = [defaultdict(lambda: -1)]*len(ads)

    print("P2: {}".format(skive_old(memory, ads)))

if __name__ == "__main__":
    main()
