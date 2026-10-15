def read_input(filename):
    rows = []
    with open(filename, "r") as f:
        for line in f:
            l = line.strip()
            if not l:
                continue

            row = [item.strip() for item in l.split(",")]
            rows.append(row)
    return rows

def solve_first_part(names, moves):
    n = len(names)
    i = 0

    for move in moves:
        if move[0] == 'L':
            i = max(0, i - int(move[1]))
        elif move[0] == 'R':
            i = min(n, i + int(move[1]))

    return names[i]

def solve_second_part(names, moves):
    n = len(names)
    i = 0
    for move in moves:
        tmp = int(move[1:]) % n
        if move[0] == 'L':
            print("left")
            if i >= tmp:
                i -= tmp
            else:
                i = i - tmp + n
        elif move[0] == 'R':
            i = (i + tmp) % n

    return names[i]

def solve_third_part(names, moves):
    n = len(names)
    print(n)
    for move in moves:
        print(names[0])
        print(move)
        tmp = int(move[1:]) % n
        i = 0
        if tmp == 0:
            continue
        if move[0] == 'L':
            i = n - tmp
        elif move[0] == 'R':
            i = i + tmp
        print(i)
        t = names[i]
        names[i] = names[0]
        names[0] = t
    return names[0]
    
def main():
    input = read_input("input1.txt")
    second_input = read_input("input2.txt")
    third_input = read_input("input3.txt")
    # names, moves = input[0], input[1]
    # names, moves = second_input[0], second_input[1]
    names, moves = third_input[0], third_input[1]
    # print(f"Result first: {solve_first_part(names, moves)}")
    # print(f"Result second: {solve_second_part(names, moves)}")
    print(solve_third_part(names, moves))

if __name__ == "__main__":
    main()
