def main():
    with open('day6.txt', 'r') as f:
        data = f.read().split("\n\n")

    p1 = []
    for d in data:
        answers = set()
        for p in d.split():
            for c in p:
                answers.add(c)
        p1.append(answers)
    print ("P1: {}".format(sum([len(r) for r in p1])))

    cnt = 0
    for idx, d in enumerate(data):
        entries = d.count("\n") + 1
        for letter in p1[idx]:
            # use set of letters per entry from p1
            if d.count(letter) == entries:
                cnt += 1
    print ("P2: {}".format(cnt))


if __name__ == "__main__":
    main()
