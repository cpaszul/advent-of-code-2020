import math

DEFAULT_INPUT = 'day5.txt'

def day_5(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        seat_ids = [get_seat_id(line.rstrip()) for line in f.readlines()]
    seat_ids.sort()
    part_1 = seat_ids[-1]
    for n in range(seat_ids[0] + 1, seat_ids[-1]):
        if n - 1 in seat_ids and n + 1 in seat_ids and n not in seat_ids:
            return part_1, n
    
def get_seat_id(seat: str) -> int:
    return get_row(seat[:-3]) * 8 + get_col(seat[-3:])

def get_row(chrs: str) -> int:
    lower, upper = 0, 127
    for c in chrs[:-1]:
        if c == 'F':
            upper = math.floor((lower + upper)/2)
        else:
            lower = math.ceil((lower + upper)/2)
    return lower if chrs[-1] == 'F' else upper

def get_col(chrs: str) -> int:
    lower, upper = 0, 7
    for c in chrs[:-1]:
        if c == 'L':
            upper = math.floor((lower + upper)/2)
        else:
            lower = math.ceil((lower + upper)/2)
    return lower if chrs[-1] == 'L' else upper
                    

if __name__ == '__main__':
    part_1, part_2 = day_5()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
