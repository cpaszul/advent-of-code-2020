from collections import defaultdict
from functools import cache

DEFAULT_INPUT = 'day10.txt'

GRAPH = defaultdict(list)

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        adapters = [0] + [int(line) for line in f.readlines()]
    adapters.append(max(adapters) + 3)
    adapters.sort()
    diffs_1 = 0
    diffs_3 = 0
    for a, b in zip(adapters, adapters[1:]):
        if b - a == 1:
            diffs_1 += 1
        if b - a == 3:
            diffs_3 += 1
    return diffs_1 * diffs_3

def part_2(loc: str = DEFAULT_INPUT) -> int:
    global GRAPH
    with open(loc) as f:
        adapters = {0} | {int(line) for line in f.readlines()}
    target = max(adapters) + 3
    adapters.add(target)
    for val in adapters:
        for n in (val + 1, val + 2, val + 3):
            if n in adapters:
                GRAPH[val].append(n)
    return paths_to_target(0, target)

@cache
def paths_to_target(start: int, target: int) -> int:
    global GRAPH
    if start == target:
        return 1
    return sum(paths_to_target(node, target) for node in GRAPH[start])

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
