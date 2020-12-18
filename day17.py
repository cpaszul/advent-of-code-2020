from collections import defaultdict

DEFAULT_INPUT = 'day17.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    cubes = defaultdict(bool)
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            row = row.rstrip()
            for x, cell in enumerate(row):
                if cell == '#':
                    cubes[(x, y, 0)] = True
    for _ in range(6):
        cubes = update_cubes_p1(cubes)
    return sum(1 for value in cubes.values() if value)

def get_neighbors_p1(x: int, y: int, z: int) -> list[tuple[int, int, int]]:
    neighbors = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if not (dx == dy == dz == 0):
                    neighbors.append((x + dx, y + dy, z + dz))
    return neighbors

def update_cubes_p1(cubes: dict[tuple[int, int, int], bool]) -> dict[tuple[int, int, int], bool]:
    new_cubes = defaultdict(bool)
    active_cubes = list(key for key, value in cubes.items() if value)
    to_update = set()
    for cube in active_cubes:
        for neighbor in get_neighbors_p1(*cube):
            to_update.add(neighbor)
    for cube in to_update:
        active_neighbors = sum(1 for neighbor in get_neighbors_p1(*cube) if cubes[neighbor])
        if cubes[cube] and active_neighbors in (2, 3):
            new_cubes[cube] = True
        if not cubes[cube] and active_neighbors == 3:
            new_cubes[cube] = True
    return new_cubes

def part_2(loc: str = DEFAULT_INPUT) -> int:
    cubes = defaultdict(bool)
    with open(loc) as f:
        for y, row in enumerate(f.readlines()):
            row = row.rstrip()
            for x, cell in enumerate(row):
                if cell == '#':
                    cubes[(x, y, 0, 0)] = True
    for _ in range(6):
        cubes = update_cubes_p2(cubes)
    return sum(1 for value in cubes.values() if value)

def get_neighbors_p2(x: int, y: int, z: int, w: int) -> list[tuple[int, int, int, int]]:
    neighbors = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if not (dx == dy == dz == dw == 0):
                        neighbors.append((x + dx, y + dy, z + dz, w + dw))
    return neighbors

def update_cubes_p2(cubes: dict[tuple[int, int, int, int], bool]) -> dict[tuple[int, int, int, int], bool]:
    new_cubes = defaultdict(bool)
    active_cubes = list(key for key, value in cubes.items() if value)
    to_update = set()
    for cube in active_cubes:
        for neighbor in get_neighbors_p2(*cube):
            to_update.add(neighbor)
    for cube in to_update:
        active_neighbors = sum(1 for neighbor in get_neighbors_p2(*cube) if cubes[neighbor])
        if cubes[cube] and active_neighbors in (2, 3):
            new_cubes[cube] = True
        if not cubes[cube] and active_neighbors == 3:
            new_cubes[cube] = True
    return new_cubes

if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
