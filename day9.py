from itertools import combinations
from collections import deque

DEFAULT_INPUT = 'day9.txt'

def day_9(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        ints = [int(line) for line in f.readlines()]
    current = 25
    target = None
    while target is None:
        current_num = ints[current]
        nums = ints[current - 25:current]
        if any(a + b == current_num for a, b in combinations(nums, 2)):
            current += 1
            continue
        target = current_num
    i = 0
    nums = deque()
    while (s := sum(nums)) != target:
        if s > target:
            nums.popleft()
        else:
            nums.append(ints[i])
            i += 1
    return target, min(nums) + max(nums)

    
if __name__ == '__main__':
    part_1, part_2 = day_9()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
