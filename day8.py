DEFAULT_INPUT = 'day8.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        lines = [((ln := line.rstrip().split(' '))[0], int(ln[1]))
                 for line in f.readlines()]
    return run(lines)[1]

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        lines = [((ln := line.rstrip().split(' '))[0], int(ln[1]))
                 for line in f.readlines()]
    for i in range(len(lines)):
        op, val = lines[i]
        if op in ('nop', 'jmp'):
            new_lines = lines.copy()
            new_op = 'nop' if op == 'jmp' else 'jmp'
            new_lines[i] = (new_op, val)
            if (res := run(new_lines))[0]:
                return res[1]
                    
def run(lines: list[tuple[str, int]]) -> tuple[bool, int]:
    seen = set()
    acc = 0
    cur = 0
    while cur < len(lines):
        if cur in seen:
            return False, acc
        seen.add(cur)
        op, val = lines[cur]
        if op == 'acc':
            acc += val
        cur += val if op == 'jmp' else 1
    return True, acc


if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
