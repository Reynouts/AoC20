from collections import deque as dq
import re
from copy import deepcopy as dc


def play(decks):
    while decks[0] and decks[1]:
        c1 = decks[0].pop()
        c2 = decks[1].pop()
        winner = 0 if c1 > c2 else 1
        if winner == 0:
            decks[0].appendleft(c1)
            decks[0].appendleft(c2)
        else:
            decks[1].appendleft(c2)
            decks[1].appendleft(c1)
    return winner, decks


def deckstostring(decks):
    res = ""
    for deck in decks:
        res += "".join(str(x) for x in list(deck)) + " "
    return res.strip()


def playtwo(decks):
    seen = set()
    while decks[0] and decks[1]:
        dts = deckstostring(decks)
        if dts in seen:
            return 0, decks
        else:
            seen.add(dts)
        c1 = decks[0].pop()
        c2 = decks[1].pop()
        if c1 <= len(decks[0]) and c2 <= len(decks[1]):
            winner, _ = playtwo([dq(list(decks[0])[-c1:]), dq(list(decks[1])[-c2:])])
        else:
            winner = 0 if c1 > c2 else 1
        if winner == 0:
            decks[0].appendleft(c1)
            decks[0].appendleft(c2)
        else:
            decks[1].appendleft(c2)
            decks[1].appendleft(c1)
    return winner, decks


def score(decks):
    if len(decks[0]) == 0:
        winner = 1
    else:
        winner = 0
    score = 0
    while decks[winner]:
        score += (len(decks[winner]) * decks[winner].pop())
    return score


def main():
    with open('day22.txt', 'r') as f:
        data = f.read()

    decks = []
    for player in data.split("\n\n"):
        deck = dq()
        player = player.split("\n")
        for line in player:
            if not "Player" in line:
                deck.appendleft(int(re.search(r'\d+', line).group()))
        decks.append(deck)

    _, d = play(dc(decks))
    print("P1: {}".format(score(d)))
    _, d = playtwo(decks)
    print("P2: {}".format(score(d)))


if __name__ == "__main__":
    main()
