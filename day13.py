import aocutils


@aocutils.timeit
def main():
    with open('day13.txt', 'r') as f:
        data = f.readlines()
    leave = int(data[0])
    buss = data[1].split(",")

    wait = 10 ** 10
    tar = -1
    print(leave)
    for bus in buss:
        if bus != "x":
            bus = int(bus)
            wt = bus - (leave % bus)
            if wt < wait:
                wait = wt
                tar = bus
    print(f"P1: {wait * tar}")

    busses = []
    for offset, bus in enumerate(buss):
        if bus != "x":
            busses.append((offset, int(bus)))

    def getfirst(step, bus, offset, start):
        hits = []
        while len(hits) != 2:
            if (start + offset) % bus == 0:
                hits.append(start)
            start += step
        low = hits[0]
        step = hits[1] - hits[0]
        return low, step

    low = step = busses[0][1]
    for bus in busses[1:]:
        offset = bus[0]
        low, step = getfirst(step, bus[1], offset, low)
    print("P2: {}".format(low))


if __name__ == "__main__":
    main()
