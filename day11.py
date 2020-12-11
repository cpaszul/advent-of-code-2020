from functools import cache

DEFAULT_INPUT = 'day11.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    with open(loc) as f:
        for y, line in enumerate(f.readlines()):
            for x, cell in enumerate(line.rstrip()):
                grid[(x, y)] = cell
    prev_grid = {}
    while True:
        grid = p1_run(grid)
        if prev_grid == grid:
            return sum(1 for cell in grid if grid[cell] == '#')
        prev_grid = grid

def p1_run(grid: dict[tuple[int, int], str]) -> dict[tuple[int, int], str]:
    new_grid = {}
    for cell in grid:
        if grid[cell] == '.':
            new_grid[cell] = '.'
        else:
            occupied_adjs = sum(1 for adj_cell in p1_adj(cell)
                                if adj_cell in grid and grid[adj_cell] == '#')
            if grid[cell] == 'L' and occupied_adjs == 0:
                new_grid[cell] = '#'
            elif grid[cell] == '#' and occupied_adjs >= 4:
                new_grid[cell] = 'L'
            else:
                new_grid[cell] = grid[cell]
    return new_grid

@cache
def p1_adj(cell: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = cell
    adjs = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                adjs.append((x + dx, y + dy))
    return adjs


def part_2(loc: str = DEFAULT_INPUT) -> int:
    grid = {}
    seats = set()
    with open(loc) as f:
        for y, line in enumerate(f.readlines()):
            for x, cell in enumerate(line.rstrip()):
                grid[(x, y)] = cell
                if cell in '#L':
                    seats.add((x, y))
    seats = frozenset(seats)
    prev_grid = {}
    while True:
        grid = p2_run(grid, seats)
        if prev_grid == grid:
            return sum(1 for cell in grid if grid[cell] == '#')
        prev_grid = grid

def p2_run(grid: dict[tuple[int, int], str], seats: frozenset[tuple[int, int]]) -> dict[tuple[int, int], str]:
    new_grid = {}
    for cell in grid:
        if grid[cell] == '.':
            new_grid[cell] = '.'
        else:
            occupied_adjs = sum(1 for adj_cell in p2_adj(cell, seats)
                                if grid[adj_cell] == '#')
            if grid[cell] == 'L' and occupied_adjs == 0:
                new_grid[cell] = '#'
            elif grid[cell] == '#' and occupied_adjs >= 5:
                new_grid[cell] = 'L'
            else:
                new_grid[cell] = grid[cell]
    return new_grid

@cache
def p2_adj(cell: tuple[int, int], seats: frozenset[tuple[int, int]]) -> list[tuple[int, int]]:
    x, y = cell
    adjs = []
    min_x = min(seats, key=lambda t:t[0])[0]
    min_y = min(seats, key=lambda t:t[1])[1]
    max_x = max(seats, key=lambda t:t[0])[0]
    max_y = max(seats, key=lambda t:t[1])[1]
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                i, j = x + dx, y + dy
                next_dir = False
                while min_x <= i <= max_x and min_y <= j <= max_y:
                    if (i, j) in seats:
                        adjs.append((i, j))
                        break
                    i += dx
                    j += dy
    return adjs

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
