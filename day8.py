import queue


def run(instructions):
    # rules dictionary, returns tuple what to do with index and accumulator
    rules = {
        "nop": lambda idx, acc, x: (idx+1, acc+0),
        "acc": lambda idx, acc, x: (idx+1, acc+x),
        "jmp": lambda idx, acc, x: (idx+x, acc+0),
    }

    acc = 0
    idx = 0
    seen = set()
    while idx not in seen:
        seen.add(idx)
        name, par = instructions[idx]
        idx, acc = rules[name](idx, acc, par)
        if idx >= len(instructions):
            # not looping, finished (p2)
            return idx, acc, True
    # looping (p1)
    return idx, acc, False


def main():
    with open('day8.txt', 'r') as f:
        data = f.readlines()

    q = queue.Queue()
    instructions = []
    for idx, line in enumerate(data):
        name, par = line.split()
        instructions.append((name, int(par)))
        if name == "nop" or name == "jmp":
            q.put((idx, name))

    print("P1: {}".format(run(instructions)[1]))

    switch = {
        "nop": "jmp",
        "jmp": "nop",
    }

    # change instructions to fix corrupt instruction
    while not q.empty():
        m_inst = list(instructions)
        pos, name = q.get()
        m_inst[pos] = (switch[name],m_inst[pos][1])
        idx, acc, found = (run(m_inst))
        if found: break
    print("P2: {}".format(acc))


if __name__ == "__main__":
    main()
