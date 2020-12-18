from functools import reduce

DEFAULT_INPUT = 'day18.txt'

def day_18(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    return sum(simplify_p1(line) for line in lines), \
           sum(simplify_p2(line) for line in lines)

def simplify_p1(line: str) -> int:
    while '(' in line:
        last_open = -1
        for i, char in enumerate(line):
            if char == '(':
                last_open = i
            if char == ')':
                simplified = simplify_p1(line[last_open + 1: i])
                line = line[:last_open] + str(simplified) + line[i + 1:]
                break
    vals = line.split(' ')
    op = None
    total = int(vals[0])
    for val in vals[1:]:
        if val == '+':
            op = lambda a, b: a + b
        elif val == '*':
            op = lambda a, b: a * b
        else:
            total = op(total, int(val))
    return total

def simplify_p2(line: str) -> int:
    while '(' in line:
        last_open = -1
        for i, char in enumerate(line):
            if char == '(':
                last_open = i
            if char == ')':
                simplified = simplify_p2(line[last_open + 1: i])
                line = line[:last_open] + str(simplified) + line[i + 1:]
                break
    sums = [sum(map(int, segment.split(' + '))) for segment in line.split(' * ')]
    return reduce(lambda a, b: a * b, sums)

if __name__ == '__main__':
    part_1, part_2 = day_18()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
