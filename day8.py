DEFAULT_INPUT = 'day8.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    seen = set()
    acc = 0
    cur = 0
    while True:
        if cur in seen:
            return acc
        seen.add(cur)
        op, val = lines[cur].split(' ')
        if op == 'acc':
            acc += int(val)
            cur += 1
        elif op == 'jmp':
            cur += int(val)
        else:
            cur += 1

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    for i in range(len(lines)):
        line = lines[i]
        op, val = line.split(' ')
        if op in ('nop', 'jmp'):
            new_lines = lines.copy()
            new_op = 'nop' if op == 'jmp' else 'jmp'
            new_lines[i] = ' '.join((new_op, val))
            if (res := finishes(new_lines))[0]:
                return res[1]
                    
def finishes(lines: list[str]) -> tuple[bool, int]:
    seen = set()
    acc = 0
    cur = 0
    while cur < len(lines):
        if cur in seen:
            return False, 0
        seen.add(cur)
        op, val = lines[cur].split(' ')
        if op == 'acc':
            acc += int(val)
            cur += 1
        elif op == 'jmp':
            cur += int(val)
        else:
            cur += 1
    return True, acc


if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
