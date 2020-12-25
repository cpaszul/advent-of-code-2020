from collections import defaultdict

DEFAULT_INPUT = 'day24.txt'

def day_24(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    tiles = defaultdict(bool)
    with open(loc) as f:
        lines = [line.rstrip() for line in f.readlines()]
    for line in lines:
        tile = move(line)
        tiles[tile] = not tiles[tile]
    part_1_res = sum(1 for value in tiles.values() if value)
    for _ in range(100):
        tiles = update(tiles)
    return part_1_res, sum(1 for value in tiles.values() if value)

def move(line: str) -> tuple[int, int]:
    i = 0
    x, y = 0, 0
    while i < len(line):
        ch = line[i]
        if ch in 'ew':
            x += (1 if ch == 'e' else -1)
            i += 1
        else:
            x += (0.5 if line[i + 1] == 'e' else -0.5)
            y += (1 if ch == 's' else -1)
            i += 2
    return x, y

def update(tiles: dict[bool]) -> dict[bool]:
    new_tiles = defaultdict(bool)
    tiles_to_update = set()
    for k, v in tiles.items():
        if v:
            tiles_to_update.add(k)
            for n in neighbors(k):
                tiles_to_update.add(n)
    for tile in tiles_to_update:
        active_neighbors = sum(1 for n in neighbors(tile) if tiles[n])
        if tiles[tile] and active_neighbors in (1, 2):
            new_tiles[tile] = True
        if not tiles[tile] and active_neighbors == 2:
            new_tiles[tile] = True
    return new_tiles

def neighbors(cell: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = cell
    return [(x + 1, y), (x - 1, y),
            (x + 0.5, y + 1), (x - 0.5, y + 1),
            (x + 0.5, y - 1), (x - 0.5, y - 1)]

    
if __name__ == '__main__':
    part_1, part_2 = day_24()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
