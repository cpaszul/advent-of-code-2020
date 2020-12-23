from collections import deque

DEFAULT_INPUT = 'day22.txt'

def part_1(loc: str = DEFAULT_INPUT) -> int:
    p1 = deque()
    p2 = deque()
    with open(loc) as f:
        p1_deck = True
        for line in f.readlines():
            if line == '\n':
                p1_deck = False
            elif line in ('Player 1:\n', 'Player 2:\n'):
                continue
            elif p1_deck:
                p1.append(int(line))
            else:
                p2.append(int(line))
    while p1 and p2:
        p1_card = p1.popleft()
        p2_card = p2.popleft()
        if p1_card > p2_card:
            p1.append(p1_card)
            p1.append(p2_card)
        else:
            p2.append(p2_card)
            p2.append(p1_card)
    if p1:
        return calc_score(p1)
    else:
        return calc_score(p2)

def calc_score(cards: deque[int]) -> int:
    i = 1
    total = 0
    while cards:
        right_card = cards.pop()
        total += (right_card * i)
        i += 1
    return total

def part_2(loc: str = DEFAULT_INPUT) -> int:
    p1 = deque()
    p2 = deque()
    with open(loc) as f:
        p1_deck = True
        for line in f.readlines():
            if line == '\n':
                p1_deck = False
            elif line in ('Player 1:\n', 'Player 2:\n'):
                continue
            elif p1_deck:
                p1.append(int(line))
            else:
                p2.append(int(line))
    return game_round(p1, p2)[1]

def game_round(p1: deque[int], p2: deque[int]) -> tuple[int, int]:
    seen_decks = set()
    while p1 and p2:
        current_state = (tuple(p1), tuple(p2))
        if current_state in seen_decks:
            return 1, p1
        seen_decks.add(current_state)
        p1_card = p1.popleft()
        p2_card = p2.popleft()
        if len(p1) >= p1_card and len(p2) >= p2_card:
            p1_subdeck = deque()
            p2_subdeck = deque()
            for i in range(p1_card):
                p1_subdeck.append(p1[i])
            for j in range(p2_card):
                p2_subdeck.append(p2[j])
            subgame_winner, _ = game_round(p1_subdeck, p2_subdeck)
            if subgame_winner == 1:
                p1.append(p1_card)
                p1.append(p2_card)
            else:
                p2.append(p2_card)
                p2.append(p1_card)
        elif p1_card > p2_card:
            p1.append(p1_card)
            p1.append(p2_card)
        else:
            p2.append(p2_card)
            p2.append(p1_card)
    if p1:
        return 1, calc_score(p1)
    else:
        return 2, calc_score(p2)
        


if __name__ == '__main__':
    print('Solution for Part One:', part_1())
    print('Solution for Part Two:', part_2())
