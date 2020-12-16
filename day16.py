from collections import defaultdict

DEFAULT_INPUT = 'day16.txt'

def day_16(loc: str = DEFAULT_INPUT) -> int:
    range_dict = defaultdict(list)
    field_names = set()
    tickets = []
    valid_tickets = []
    invalid_total = 0
    with open(loc) as f:
        segment = 1
        for line in f.readlines():
            if line == '\n':
                segment += 1
            elif segment == 1:
                name, ranges = line.rstrip().split(': ')
                field_names.add(name)
                for r in ranges.split(' or '):
                    start, end = r.split('-')
                    range_dict[name].append(range(int(start), int(end) + 1))
            elif segment == 2:
                if line == 'your ticket:\n':
                    continue
                my_ticket = list(map(int, line.split(',')))
                tickets.append(my_ticket)
            else:
                if line == 'nearby tickets:\n':
                    continue
                tickets.append(list(map(int, line.split(','))))
    for ticket in tickets:
        valid_ticket = True
        for num in ticket:
            if not any(in_ranges(num, ranges) for ranges in range_dict.values()):
                invalid_total += num
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(ticket)
    part_1_res = invalid_total
    fields = [field_names.copy() for _ in range(len(my_ticket))]
    for ticket in valid_tickets:
        for field_index, num in enumerate(ticket):
            valid = valid_ranges(num, range_dict)
            fields[field_index] &= valid
    fields = solve_fields(fields)
    part_2_res = 1
    for field_name, ticket_value in zip(fields, my_ticket):
        if field_name.startswith('departure'):
            part_2_res *= ticket_value
    return part_1_res, part_2_res

def in_ranges(num: int, ranges: list[list[int]]) -> bool:
    for r in ranges:
        if num in r:
            return True
    return False

def valid_ranges(num: int, range_dict: dict[str, list[list[int]]]) -> set[str]:
    valid = set()
    for name, ranges in range_dict.items():
        if in_ranges(num, ranges):
            valid.add(name)
    return valid

def solve_fields(fields: list[set[str]]) -> list[str]:
    solved = set()
    for _ in range(30):
        for index, field in enumerate(fields):
            if isinstance(field, set):
                field -= solved
                if len(field) == 1:
                    value = list(field)[0]
                    fields[index] = value
                    solved.add(value)
    return fields
                

if __name__ == '__main__':
    part_1, part_2 = day_16()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
