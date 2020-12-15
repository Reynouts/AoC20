import aocutils


@aocutils.timeit
def main():
    data = [7,14,0,17,11,1,2]
    p1 = 2020
    p2 = 30000000
    numbers = dict(zip(data[:-1], range(len(data)-1)))

    last = data[len(data)-1]
    for cnt in range(len(data), p2):
        if cnt == p1: print(f"P1: {last}")
        t = cnt-1 - numbers[last] if last in numbers else 0
        numbers[last] = cnt - 1
        last = t
    print(f"P2: {last}")


if __name__ == "__main__":
    main()
