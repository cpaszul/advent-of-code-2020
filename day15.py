from collections import defaultdict

DEFAULT_INPUT = 'day15.txt'

def day_15(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    with open(loc) as f:
        starting_numbers = list(map(int, f.readline().split(',')))
    spoken = defaultdict(list)
    turn = 1
    last_number = None
    while True:
        if turn <= len(starting_numbers):
            spoken_number = starting_numbers[turn - 1]
        else:
            if len(spoken[last_number]) == 1:
                spoken_number = 0
            else:
                spoken_number = spoken[last_number][-1] - spoken[last_number][-2]
        if turn == 2020:
            p1_res = spoken_number
        if turn == 30000000:
            return p1_res, spoken_number
        spoken[spoken_number].append(turn)
        last_number = spoken_number
        turn += 1

if __name__ == '__main__':
    part_1, part_2 = day_15()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
