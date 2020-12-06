DEFAULT_INPUT = 'day6.txt'

def day_6(loc: str = DEFAULT_INPUT) -> int:
    part_1 = 0
    part_2 = 0
    with open(loc) as f:
        answers = ''
        group_size = 0
        for line in f.readlines():
            if line == '\n':
                common_answers = set()
                for char in answers:
                    if answers.count(char) == group_size:
                        common_answers.add(char)
                part_1 += len(set(answers))
                part_2 += len(set(common_answers))
                answers = ''
                group_size = 0
            else:
                answers += line.rstrip()
                group_size += 1
        if answers:
            common_answers = set()
            for char in answers:
                if answers.count(char) == group_size:
                    common_answers.add(char)
            part_1 += len(set(answers))
            part_2 += len(set(common_answers))
    return part_1, part_2
                    

if __name__ == '__main__':
    part_1, part_2 = day_6()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
