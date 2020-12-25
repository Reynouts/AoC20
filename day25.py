def encrypt(target, key, t1=7, m=20201227):
    v1 = v2 = 1
    while v1 != target:
        v1 = (v1 * t1) % m
        v2 = (v2 * key) % m
    return v2


def main():
    with open('day25.txt', 'r') as f:
        print(encrypt(*list(map(int, f.readlines()))))


if __name__ == "__main__":
    main()
