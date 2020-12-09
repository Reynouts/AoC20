import re


def get_parents(rules, bag):
    result = set()
    for rule in rules:
        if bag in [x[0] for x in rules[rule]]:
            result.add(rule)
    if result:
        for i in result.copy():
            future = get_parents(rules, i)
            if future:
                result.update(future)
        return result


def count_bags(info, bag):
    n = 0
    if bag in info.keys():
        childs = info[bag]
        for child in childs:
            n += child[1] + count_bags(info, child[0])*child[1]
    return n


def main():
    with open('day7.txt', 'r') as f:
        data = f.readlines()

    info = dict()
    for rule in data:
        if "no other bags" not in rule:
            inbag = re.match("\w+\s\w+", rule)[0]
            outbags = re.findall("((\d+)\s(\w+\s\w+)\sbags?)(?:,|.)", rule)
            info[inbag] = [(outbag[2], int(outbag[1])) for outbag in outbags]

    goal = "shiny gold"
    print("P1: {}".format(len(get_parents(info, goal))))
    print("P2: {}".format(count_bags(info, goal)))


if __name__ == "__main__":
    main()
