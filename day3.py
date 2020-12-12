from functools import reduce

DEFAULT_INPUT = 'day3.txt'

def tree_count(dx: int, dy: int, height: int, width: int,
               grid: dict[tuple[int, int], str]) -> int:
    x, y = 0, 0
    trees = 0
    while y < height:
        if grid[(x, y)] == '#':
            trees += 1
        y += dy
        x += dx
        x %= width
    return trees

def day_3(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    grid = {}
    height = 0
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            height += 1
            width = len(row.rstrip())
            for x, cell in enumerate(row.rstrip()):
                grid[(x, y)] = cell
    part_1 = tree_count(3, 1, height, width, grid)
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    part_2 = reduce(lambda x, y: x * y,
                    (tree_count(dx, dy, height, width, grid) for dx, dy in slopes),
                    1)
    return part_1, part_2

if __name__ == '__main__':
    part_1, part_2 = day_3()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
