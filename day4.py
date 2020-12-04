import re


def parse(data, fields):
    files = []
    for pwd in data:
        pwdfields = {}
        for field in fields:
            # running python 3.7, but from 3.8 wallrus!
            field_search = re.search(field + ':(.+?)(\s|$)', pwd)
            if field_search:
                pwdfields[field] = field_search.group(1)
        files.append(pwdfields)
    return files


def bounds(entry, l, low, hi):
    return len(entry) == l and entry.isdigit() and low <= int(entry) <= hi


def hgt(entry):
    if entry.endswith("cm"):
        return bounds(entry.split("cm")[0], 3, 150, 193)
    elif entry.endswith("in"):
        return bounds(entry.split("in")[0], 2, 59, 76)
    return False


def validate(files, fields):
    p1 = 0
    p2 = 0
    for file in files:
        # check all fields except optional "cid", which is the last in the dictionary
        #   dicts are ordered from 3.7 so is OK, but not very maintainable :)
        if all(field in file.keys() for field in list(fields)[:-1]):
            p1 += 1
            if all(fields[field](file[field]) for field in list(fields)[:-1]):
                p2 += 1
    return p1, p2


def main():
    with open('day4.txt', 'r') as f:
        data = f.read().split("\n\n")

    fields = {
        "byr": lambda x: bounds(x, 4, 1920, 2002),
        "iyr": lambda x: bounds(x, 4, 2010, 2020),
        "eyr": lambda x: bounds(x, 4, 2020, 2030),
        "hgt": hgt,
        "hcl": lambda x: re.match('^#([a-f]|\d){6}$', x),
        "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda x: re.match('^\d{9}$', x),
        "cid": True # last in dict!
    }

    files = parse(data, fields)
    p1, p2 = validate(files, fields)
    print("Part 1: {}".format(p1))
    print("Part 2: {}".format(p2))


if __name__ == "__main__":
    main()
