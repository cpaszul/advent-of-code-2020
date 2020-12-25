DEFAULT_INPUT = 'day23.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        cups = list(map(int, (ch for ch in f.readline().rstrip())))
    cup_dict = {}
    for a, b in zip(cups, cups[1:]):
        cup_dict[a] = b
    cup_dict[cups[-1]] = cups[0]
    current_cup = cups[0]
    for _ in range(100):
        cups_to_move = [(move_a := cup_dict[current_cup]),
                        (move_b := cup_dict[move_a]),
                        (move_c := cup_dict[move_b])]
        destination_found = False
        target = current_cup - 1
        while not destination_found:
            if target > 0 and target not in cups_to_move:
                destination_found = True
            else:
                target -= 1
                if target < 1:
                    target = max(cup_dict)
        cup_dict[current_cup] = cup_dict[cups_to_move[-1]]
        cup_dict[cups_to_move[-1]] = cup_dict[target]
        cup_dict[target] = cups_to_move[0]
        current_cup = cup_dict[current_cup]
    result = ''
    current = 1
    while True:
        result += str(cup_dict[current])
        current = cup_dict[current]
        if current == 1:
            break
    return result[:-1]
                
    
def part_2(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        cups = list(map(int, (ch for ch in f.readline().rstrip())))
    while len(cups) < 1_000_000:
        cups.append(len(cups) + 1)
    cup_dict = {}
    for a, b in zip(cups, cups[1:]):
        cup_dict[a] = b
    cup_dict[cups[-1]] = cups[0]
    current_cup = cups[0]
    for _ in range(10_000_000):
        cups_to_move = [(move_a := cup_dict[current_cup]),
                        (move_b := cup_dict[move_a]),
                        (move_c := cup_dict[move_b])]
        destination_found = False
        target = current_cup - 1
        while not destination_found:
            if target > 0 and target not in cups_to_move:
                destination_found = True
            else:
                target -= 1
                if target < 1:
                    target = max(cup_dict)
        cup_dict[current_cup] = cup_dict[cups_to_move[-1]]
        cup_dict[cups_to_move[-1]] = cup_dict[target]
        cup_dict[target] = cups_to_move[0]
        current_cup = cup_dict[current_cup]    
    return (i := cup_dict[1]) * cup_dict[i]

    
if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
