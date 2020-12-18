import re


# mess with the precedence of the operators
class hint:
    def __init__(self, n):
        self.n = n

    def __mul__(self, other):
        return hint(self.n * other.n)

    def __floordiv__(self, other):
        return hint(self.n + other.n)

    def __sub__(self, other):
        return hint(self.n * other.n)

    def __str__(self):
        return str(self.n)


def solve(data, replaces):
    res = 0
    for line in data:
        line = re.sub('(\d+)', r'hint(\1)', line)
        for r in replaces:
            line = line.replace(r, replaces[r])
        res += (int(str(eval(line))))
    return res


def main():
    with open('day18.txt', 'r') as f:
        data = f.readlines()
    r1 = {"+": "//"}
    print("P1: {}".format(solve(data, r1)))
    r2 = {"*": "-", "+": "//"}
    print("P2: {}".format(solve(data, r2)))


if __name__ == "__main__":
    main()
