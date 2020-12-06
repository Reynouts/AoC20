

def main():
    with open('day5.txt', 'r') as f:
        data = f.read().split()

    seats = []
    for pp in data:
        row = (0, 127)
        col = (0, 7)
        for c in pp:
            shift_rows = (row[1] - row[0] + 1) // 2
            shift_cols = (col[1] - col[0] + 1) // 2
            if c == "F":
                row = (row[0], row[1] - shift_rows)
            elif c == "B":
                row = (row[0] + shift_rows, row[1])
            elif c == "L":
                col = (col[0], col[1] - shift_cols)
            elif c == "R":
                col = (col[0] + shift_cols, col[1])
        seats.append(row[0] * 8 + col[0])

    seats = sorted(seats)
    start = seats[0]
    for idx, seat in enumerate(seats):
        if seat != idx+start:
            p2 = seat-1
            break

    print("Part 1: {}".format(seats[-1]))
    print("Part 2: {}".format(p2))


if __name__ == "__main__":
    main()
