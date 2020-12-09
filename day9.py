def check(pre, target):
    pool = set(pre)
    for p in pre:
        if target-p in pool:
            return True
    return False


def main():
    with open('day9.txt', 'r') as f:
        data = list(map(int, f.readlines()))

    shift = 25

    for i in range(shift, len(data)):
        if not (check(data[i-shift:i], data[i])):
            break
    p1_index = i
    p1_value = data[i]
    print("P1: {}".format(p1_value))

    for i in range(p1_index-1, 0, -1):
        if data[i] < p1_value:
            elems = [data[i]]
            counter = i
            while sum(elems) < p1_value and counter > 0:
                counter -= 1
                elems.append(data[counter])
            if sum(elems) == p1_value:
                s = sorted(elems)
                p2_value = s[0]+s[-1]
                break
    print("P2: {}".format(p2_value))


if __name__ == "__main__":
    main()
