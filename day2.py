import re

DEFAULT_INPUT = 'day2.txt'

def day_2(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
    def xor(a, b):
        return (a and not b) or (not a and b)
    with open(loc) as f:
        lines = (line.rstrip() for line in f.readlines())
    part_1, part_2 = 0, 0
    for line in lines:
        m = pattern.match(line)
        first_val = int(m.group(1))
        second_val = int(m.group(2))
        char = m.group(3)
        password = m.group(4)
        if first_val <= password.count(char) <= second_val:
            part_1 += 1
        if xor(password[first_val - 1] == char,
               password[second_val - 1] == char):
            part_2 += 1
    return part_1, part_2

if __name__ == '__main__':
    part_1, part_2 = day_2()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
