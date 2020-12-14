from collections import defaultdict
from itertools import product

DEFAULT_INPUT = 'day14.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        lines = list(line.rstrip() for line in f.readlines())
    memory = defaultdict(int)
    mask = None
    for line in lines:
        command, value = line.split(' = ')
        if command == 'mask':
            mask = value
        else:
            addr = command[4:-1]
            memory[addr] = apply_mask_p1(mask, int(value))
    return sum(memory.values())

def apply_mask_p1(mask: str, value: int) -> int:
    bin_value = bin(value)[2:].zfill(len(mask))
    masked_value = ''
    for mask_n, value_n in zip(mask, bin_value):
        if mask_n == 'X':
            masked_value += value_n
        else:
            masked_value += mask_n
    return int(masked_value, 2)

def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        lines = list(line.rstrip() for line in f.readlines())
    memory = defaultdict(int)
    mask = None
    for line in lines:
        command, value = line.split(' = ')
        if command == 'mask':
            mask = value
        else:
            addr = int(command[4:-1])
            addrs_to_write = apply_mask_p2(mask, addr)
            for new_addr in addrs_to_write:
                memory[new_addr] = int(value)
    return sum(memory.values())

def apply_mask_p2(mask: str, addr: int) -> list[int]:
    bin_addr = bin(addr)[2:].zfill(len(mask))
    masked_addr = ''
    for mask_n, addr_n in zip(mask, bin_addr):
        if mask_n in '1X':
            masked_addr += mask_n
        else:
            masked_addr += addr_n
    return expand_floats(masked_addr)

def expand_floats(addr: str) -> list[int]:
    floating_bits = addr.count('X')
    combos = list(product('10', repeat=floating_bits))
    addrs = []
    for bits in combos:
        i = 0
        new_addr = ''
        for char in addr:
            if char == 'X':
                new_addr += bits[i]
                i += 1
            else:
                new_addr += char
        addrs.append(int(new_addr, 2))
    return addrs


if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
