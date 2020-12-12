from string import ascii_lowercase

DEFAULT_INPUT = 'day6.txt'

def day_6(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    part_1 = 0
    part_2 = 0
    with open(loc) as f:
        groups = ''.join(f.readlines()).split('\n\n')
    for group in groups:
        group = group.rstrip()
        union = set()
        intersect = set(ascii_lowercase)
        for answers in group.split('\n'):
            union |= set(answers)
            intersect &= set(answers)
        part_1 += len(union)
        part_2 += len(intersect)
    return part_1, part_2
                    

if __name__ == '__main__':
    part_1, part_2 = day_6()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
