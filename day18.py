# first solution
def som(args):
    if args[1] == "+":
        return str(int(args[0]) + int(args[2]))
    elif args[1] == "*":
        return str(int(args[0]) * int(args[2]))


# was also looking for numbers bigger than 9, but that wasn't necessary
# would make it easier without that flow
def calc(line, index=0):
    args = []
    t = ""
    answer = ""
    while index <= len(line):
        dig = True
        if index == len(line) or line[index] == " " or line[index] == ")":
            if t != "":
                args.append(t)
                t = ""
            if len(args) == 3:
                answer = som(args)
                args = [answer]
            index += 1
            if index <= len(line) and line[index-1] == ")":
                if len(args) == 1:
                    answer = args[0]
                return answer, index
        elif line[index].isdigit():
            t += line[index]
            index += 1
        elif line[index] in "*+":
            args.append(line[index])
            index += 1
        elif line[index] == "(":
            answer, index = calc(line, index+1)
            if len(args) == 2:
                args.append(answer)
            else:
                args = [answer]
    return answer, index

#####
import re

# mess with the precedence of the operators
class hint:
    def __init__(self, n): self.n = n
    def __mul__(self, o): return hint(self.n * o.n)
    def __floordiv__(self, o): return hint(self.n + o.n)
    def __sub__(self, o): return hint(self.n * o.n)
    def __str__(self): return str(self.n)


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
