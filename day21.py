def main():
    with open('day21.txt', 'r') as f:
        data = f.readlines()

    allers = {}
    ingrs = {}
    for line in data:
        ing, alls = line.strip().split("(contains ")
        ing = ing.split()
        alls = alls[:-1].split(", ")

        for a in alls:
            if a in allers:
                allers[a] = allers[a].intersection(set(ing))
            else:
                allers[a] = set(ing)

        for i in ing:
            if i in ingrs:
                ingrs[i] += 1
            else:
                ingrs[i] = 1

    total = set()
    for a in allers:
        for i in allers[a]:
            total.add(i)
    p1 = 0
    for i in ingrs:
        if i not in total:
            p1 += ingrs[i]

    print("P1: {}".format(p1))

    solved = {}
    while len(solved) != len(allers):
        for a in allers:
            if len(allers[a]) == 1:
                solved[a] = allers[a].pop()
                for x in allers:
                    if solved[a] in allers[x]:
                        allers[x].remove(solved[a])
                break

    res = ""
    for i in sorted(solved.keys()):
        res += solved[i]+","
    print ("P2: {}".format(res[:-1]))






if __name__ == "__main__":
    main()
