from collections import defaultdict
from functools import cache
import re

DEFAULT_INPUT = 'day7.txt'

#global to allow caching contains_target
RULES = defaultdict(list)

def day_7(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    global RULES
    colors = set()
    pattern = re.compile(r'(\d+) (\w+ \w+)')
    with open(loc) as f:
        for line in f.readlines():
            line = line.rstrip('.\n')
            source, contents = line.split(' bags contain ')
            colors.add(source)
            for number, color in pattern.findall(contents):
                RULES[source].append((int(number), color))
    part_1 = sum(1 for color in colors if contains_target(color, 'shiny gold'))
    part_2 = contains_count('shiny gold')
    return part_1, part_2

@cache            
def contains_target(current: str, target: str) -> bool:
    global RULES
    if not RULES[current]:
        return False
    for number, color in RULES[current]:
        if color == target or contains_target(color, target):
            return True
    return False

@cache
def contains_count(current: str) -> bool:
    global RULES
    if not RULES[current]:
        return 0
    return sum(number * (contains_count(color) + 1)
               for number, color in RULES[current])
                    

if __name__ == '__main__':
    part_1, part_2 = day_7()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
