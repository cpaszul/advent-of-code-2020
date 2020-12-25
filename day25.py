DEFAULT_INPUT = 'day25.txt'

def day_25(loc: str = DEFAULT_INPUT) -> int:
    with open(loc) as f:
        card_pub_key = int(f.readline())
        door_pub_key = int(f.readline())
    card_loop_size = loop_size(card_pub_key)
    return loop(door_pub_key, card_loop_size)

def loop_size(key: int) -> int:
    value = 1
    i = 0
    while value != key:
        value *= 7
        value %= 20201227
        i += 1
    return i

def loop(subject_number: int, times: int) -> int:
    value = 1
    for _ in range(times):
        value *= subject_number
        value %= 20201227
    return value

    
if __name__ == '__main__':
    print('Solution for Part One:', day_25())
