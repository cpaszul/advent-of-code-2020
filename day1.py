DEFAULT_INPUT = 'day1.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        vals = list(map(int, f.readlines()))
    valset = set(vals)
    for val in vals:
        if (2020 - val) in valset:
            return val * (2020 - val)

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        vals = list(map(int, f.readlines()))
    valset = set(vals)
    for a, val_a in enumerate(vals[:-2]):
        for val_b in vals[a + 1:-1]:
            if (2020 - val_a - val_b) in valset:
                return val_a * val_b * (2020 - val_a - val_b)
                    

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
