

def main():
    test = "193467258"

    inp = list(map(int, test))
    current = inp[0]

    t = {}
    for i, e in enumerate(inp):
        if i+1 >= len(inp):
            t[e] = inp[0]
        else:
            t[e] = inp[i+1]

    last = inp[-1]
    for i in range(1, 1000000+1):
        if i not in t:
            t[last] = i
            last = i
    t[last] = current

    hi = max(t)
    lo = min(t)
    print(lo,hi)

    for cnt in range(10000000):
        pickup = []
        c = current
        for i in range(3):
            pickup.append(t[current])
            current = pickup[-1]
        t[c] = t[pickup[-1]]

        destination = c
        if destination == 1:
            destination = hi
        else:
            destination = c-1
        while destination in pickup:
            if destination == 1:
                destination = hi
            else:
                destination -= 1
        t[pickup[-1]] = t[destination]
        t[destination] = pickup[0]
        current = t[c]
        if cnt%1000000 == 0:
            print(cnt)

    current = 1
    res = ""
    for i in range(8):
        res += str(t[current])
        current = t[current]
    print(res)
    p2 = t[1] * t[t[1]]
    print(p2)



if __name__ == "__main__":
    main()
