from collections import Counter
from functools import reduce
from math import sqrt

DEFAULT_INPUT = 'day20.txt'

class Tile:
    def __init__(self, tile_id: int, grid: list[list[int]]):
        self.tile_id = tile_id
        self.grid = grid
        self.size = len(self.grid)
        self.top = self.grid[0]
        self.bottom = self.grid[-1]
        self.right = ''.join(self.grid[n][-1] for n in range(self.size))
        self.left = ''.join(self.grid[n][0] for n in range(self.size))
        self.edges = [self.top, self.right, self.bottom, self.left]
        self.borderless_grid = [row[1:-1] for row in self.grid[1:-1]]

def day_20(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    base_tiles = []
    with open(loc) as f:
        t_id = None
        g = []
        for line in f.readlines():
            if line == '\n':
                base_tiles.append(Tile(t_id, g))
                g = []
            elif line.startswith('Tile'):
                t_id = int(line.lstrip('Tile ').rstrip(':\n'))
            else:
                g.append(line.rstrip())
        if g:
            base_tiles.append(Tile(t_id, g))
    all_tiles = []
    for t in base_tiles:
        tid = t.tile_id
        t90 = Tile(tid, rotate_grid(t.grid))
        t180 = Tile(tid, rotate_grid(t90.grid))
        t270 = Tile(tid, rotate_grid(t180.grid))
        r = Tile(tid, reverse_grid(t.grid))
        r90 = Tile(tid, rotate_grid(r.grid))
        r180 = Tile(tid, rotate_grid(r90.grid))
        r270 = Tile(tid, rotate_grid(r180.grid))
        all_tiles.append(t)
        all_tiles.append(t90)
        all_tiles.append(t180)
        all_tiles.append(t270)
        all_tiles.append(r)
        all_tiles.append(r90)
        all_tiles.append(r180)
        all_tiles.append(r270)
    edge_counter = Counter()
    for t in all_tiles:
        for edge in t.edges:
            edge_counter[edge] += 1
    corners = []
    corner_ids = set()
    for t in all_tiles:
        if sum(1 for edge in t.edges if edge_counter[edge] == 4) == 2:
            corners.append(t)
            corner_ids.add(t.tile_id)
    p = assemble_picture(all_tiles, edge_counter)
    p90 = rotate_grid(p)
    p180 = rotate_grid(p90)
    p270 = rotate_grid(p180)
    rp = reverse_grid(p)
    rp90 = rotate_grid(rp)
    rp180 = rotate_grid(rp90)
    rp270 = rotate_grid(rp180)
    pictures = [p, p90, p180, p270, rp, rp90, rp180, rp270]
    sea_monsters = [s for picture in pictures if (s := sea_monster_count(picture)) != 0][0]
    tile_count = sum(row.count('#') for row in p)
    return reduce(lambda x, y: x * y, corner_ids), tile_count - (sea_monsters * 15)

def rotate_grid(grid: list[list[str]]) -> list[list[str]]:
    size = len(grid)
    new_grid = []
    for y in range(size):
        row = ''
        for x in range(size):
            row += grid[size - x - 1][y]
        new_grid.append(row)
    return new_grid

def reverse_grid(grid: list[list[str]]) -> list[list[str]]:
    size = len(grid)
    new_grid = [grid[y][::-1] for y in range(size)]
    return new_grid

def assemble_picture(tiles: list[Tile], edge_counter: Counter) -> list[list[Tile]]:
    picture_edges = set(k for k,v in edge_counter.items() if v == 4)
    picture = []
    top_left = [t for t in tiles if t.top in picture_edges and t.left in picture_edges][0]
    side_length = int(sqrt(len(tiles) // 8))
    borderless_tile_size = tiles[0].size - 2
    used_ids = set()
    for y in range(side_length):
        row = []
        for x in range(side_length):
            if x == 0 and y == 0:
                row.append(top_left)
                used_ids.add(top_left.tile_id)
            elif x == 0: # left edge
                top_tile = picture[y - 1][0]
                needed_tile = [t for t in tiles
                               if t.left in picture_edges and
                               t.top == top_tile.bottom and
                               t.tile_id not in used_ids][0]
                row.append(needed_tile)
                used_ids.add(needed_tile.tile_id)
            elif y == 0: # top edge
                left_tile = row[-1]
                needed_tile = [t for t in tiles
                               if t.top in picture_edges and
                               t.left == left_tile.right and
                               t.tile_id not in used_ids][0]
                row.append(needed_tile)
                used_ids.add(needed_tile.tile_id)
            else:
                top_tile = picture[y - 1][x]
                left_tile = row[-1]
                needed_tile = [t for t in tiles
                               if t.top == top_tile.bottom and
                               t.left == left_tile.right and
                               t.tile_id not in used_ids][0]
                row.append(needed_tile)
                used_ids.add(needed_tile.tile_id)
        picture.append(row)
    joined_picture = []
    for tile_row in picture:
        for y in range(borderless_tile_size):
            row = ''
            for tile in tile_row:
                row += tile.borderless_grid[y]
            joined_picture.append(row)
    return joined_picture
                         
'''
 | | | | | | | | | | | | | | | | | |#| |
#| | | | |#|#| | | | |#|#| | | | |#|#|#|
 |#| | |#| | |#| | |#| | |#| | |#| | | |
20x3
row 0: 18
row 1: 0,5,6,11,12,17,18,19
row 2: 1,4,7,10,13,16
15 tiles in total
'''

def sea_monster_count(picture: list[list[str]]) -> int:
    total = 0
    size = len(picture)
    sea_monster_tiles = [(18, 0),
                         (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1),
                         (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]
    for y in range(size - 2):
        for x in range(size - 19):
            if all(picture[y + dy][x + dx] == '#' for dx, dy in sea_monster_tiles):
                total += 1
    return total


if __name__ == '__main__':
    part_1, part_2 = day_20()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
