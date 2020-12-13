from functools import reduce

DEFAULT_INPUT = 'day13.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        earliest_timestamp = int(f.readline().rstrip())
        bus_ids = list(int(bus_id) for bus_id in f.readline().rstrip().split(',') if bus_id != 'x')
    depatures = {}
    for bus in bus_ids:
        n = bus
        while n < earliest_timestamp:
            n += bus
        depatures[bus] = n
    min_id, min_time = min(depatures.items(), key=lambda t:t[1])
    return min_id * (min_time - earliest_timestamp)

def part_2(loc: str = DEFAULT_INPUT) -> int:
    #crt based on https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    with open(loc) as f:
        _ = f.readline()
        bus_ids = list((int(bus_id), n)
                       for n, bus_id in enumerate(f.readline().rstrip().split(','))
                       if bus_id != 'x')
    n = [bus_id for bus_id, order in bus_ids]
    a = [-1 * order for bus_id, order in bus_ids]
    return crt(n, a)

def crt(n: list[int], a: list[int]) -> int:
    total = 0
    product = reduce(lambda x, y: x * y, n)
    for n_i, a_i in zip(n, a):
        p = product // n_i
        total += a_i * mul_inv(p, n_i) * p
    return total % product
 
def mul_inv(x: int, y: int) -> int:
    y_0 = y
    n_0, n_1 = 0, 1
    if y == 1:
        return 1
    while x > 1:
        q = x // y
        x, y = y, x % y
        n_0, n_1 = n_1 - q * n_0, n_0
    if n_1 < 0:
        n_1 += y_0
    return n_1

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
