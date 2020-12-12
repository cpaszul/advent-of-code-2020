DEFAULT_INPUT = 'day12.txt'

def day_12(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        moves = [(line[0], int(line[1:])) for line in f.readlines()]
    return move_ship(moves, False), move_ship(moves, True)

def move_ship(moves: list[tuple[str, int]], part_two: bool) -> int:
    x, y = 0, 0
    if part_two:
        dx, dy = 10, -1
    else:
        dx, dy = 1, 0
    for action, value in moves:
        if action == 'N':
            if part_two:
                dy -= value
            else:
                y -= value
        elif action == 'S':
            if part_two:
                dy += value
            else:
                y += value
        elif action == 'E':
            if part_two:
                dx += value
            else:
                x += value
        elif action == 'W':
            if part_two:
                dx -= value
            else:
                x -= value
        elif action == 'L':
            if value == 90:
                dx, dy = dy, -1 * dx
            elif value == 180:
                dx, dy = -1 * dx, -1 * dy
            else:
                dx, dy = -1 * dy, dx
        elif action == 'R':
            if value == 90:
                dx, dy = -1 * dy, dx
            elif value == 180:
                dx, dy = -1 * dx, -1 * dy
            else:
                dx, dy = dy, -1 * dx
        else:
            x += (dx * value)
            y += (dy * value)
    return abs(x) + abs(y)

if __name__ == '__main__':
    part_1, part_2 = day_12()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
