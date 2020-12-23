from functools import cache

RULES = {}
DEFAULT_INPUT = 'day19.txt'

def day_19(loc: str = DEFAULT_INPUT) -> tuple[int, int]:
    global RULES
    messages = []
    with open(loc) as f:
        first_segment = True
        for line in f.readlines():
            if line == '\n':
                first_segment = False
            elif first_segment:
                rule_num, rule = line.rstrip().split(': ')
                if rule.startswith('"'):
                    rule = rule[1]
                RULES[int(rule_num)] = rule
            else:
                messages.append(line.rstrip())
    part_1_res = 0
    part_2_res = 0
    for message in messages:
        if match_num(message, 0):
            part_1_res += 1
    match_num.cache_clear()
    match_rule.cache_clear()
    RULES[8] = '42 | 42 8'
    RULES[11] = '42 31 | 42 11 31'
    for message in messages:
        if match_num(message, 0):
            part_2_res += 1
    return part_1_res, part_2_res

@cache
def match_num(input_string: str, rule_num: int) -> bool:
    rule = RULES[rule_num]
    if '|' in rule:
        first_half, second_half = rule.split(' | ')
        return match_rule(input_string, first_half) or match_rule(input_string, second_half)
    else:
        return match_rule(input_string, rule)

@cache
def match_rule(input_string: str, rule: str) -> bool:
    if rule.isalpha():
        return input_string == rule
    rule_nums = list(map(int, rule.split(' ')))
    if len(rule_nums) == 1:
        return match_num(input_string, rule_nums[0])
    elif len(rule_nums) == 2:
        for i in range(1, len(input_string)):
            substring_a, substring_b = input_string[:i], input_string[i:]
            if match_num(substring_a, rule_nums[0]) and match_num(substring_b, rule_nums[1]):
                return True
        return False   
    else: #len(rule_nums) == 3, no cases of 4 or more
        for i in range(1, len(input_string)):
            substring_a, rest = input_string[:i], input_string[i:]
            for j in range(1, len(rest)):
                substring_b, substring_c = rest[:j], rest[j:]
                if match_num(substring_a, rule_nums[0]) and \
                   match_num(substring_b, rule_nums[1]) and \
                   match_num(substring_c, rule_nums[2]):
                    return True
        return False

if __name__ == '__main__':
    part_1, part_2 = day_19()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
