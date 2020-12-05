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
    return to_bin(seat[:-3]) * 8 + to_bin(seat[-3:])

def to_bin(chars: str) -> int:
    return int(''.join('1' if c in 'BR' else '0'
                       for c in chars), 2)
                    

if __name__ == '__main__':
    part_1, part_2 = day_5()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
