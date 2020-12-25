def loopsize(target, v1=1, t1=7):
    cnt = 0
    while v1 != target:
        v1 = (v1 * t1) % 20201227
        cnt += 1
    return cnt


def encrypt(key, n, v1=1):
    for _ in range(n):
        v1 = (v1 * key) % 20201227
    return v1


def main():
    with open('day25.txt', 'r') as f:
        k1, k2 = list(map(int, f.readlines()))
    print(encrypt(k2, loopsize(k1)))


if __name__ == "__main__":
    main()
