import aocutils
import re


@aocutils.timeit
def main():
    with open('day16.txt', 'r') as f:
        data = f.readlines()

    # parse rules and tickets
    rules = []
    tickets = []
    departures = []
    for line in data:
        nms = list(map(int, re.findall("\d+", line)))
        if len(nms) == 4:
            rule = set()
            for i in list(range(nms[0], nms[1]+1)) + list(range(nms[2], nms[3]+1)):
                rule.add(i)
            rules.append(rule)
            if "departure" in line:
                departures.append(len(rules)-1)
        elif len(nms) > 1:
            tickets.append(nms)

    # part 1: calculate sum of all invalid fields
    own = tickets[0]
    nearby = tickets[1:]
    validnearby = []
    valid = set.union(*rules)
    cnt = 0
    for t in nearby:
        v = True
        for n in t:
            if n not in valid:
                cnt += n
                v = False
        if v:
            validnearby.append(t)
    print(f"P1: {cnt}")

    # need some new datastructures with a id/index for rules and nearby tickets
    roels = {}
    for i, rule in enumerate(rules):
        roels[i] = rule
    nearby = {}
    for i, v in enumerate(validnearby):
        nearby[i] = v
    matrix = [[0 for x in range(len(rules))] for y in range(len(rules))]

    # helper to check if a column is valid for a given rule
    def check(r, c):
        for n in nearby:
            if nearby[n][c] not in roels[r]:
                return 0
        return 1

    # check all cells in matrix (rule/col)
    for r, rule in enumerate(matrix):
        for c, column in enumerate(rule):
            matrix[r][c] = check(r, c)

    # deduce which col matches which rule
    solved = {}
    scols = set()
    while len(solved.keys()) < len(matrix[0]):
        for r, rule in enumerate(matrix):
            if r not in solved.keys():
                vals = []
                for c, column in enumerate(rule):
                    if c not in scols and matrix[r][c] == 1:
                        vals.append(c)
                        if len(vals)> 1:
                            break
                if len(vals) == 1:
                    solved[r] = vals[0]
                    scols.add(vals[0])

    # multiply the asked fields of own ticket
    res = 1
    for i in [solved[i] for i in departures]:
        res *= own[i]
    print(f"P2: {res}")


if __name__ == "__main__":
    main()
