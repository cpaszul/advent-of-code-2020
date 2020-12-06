import re

DEFAULT_INPUT = 'day4.txt'

def day_4(loc: str = DEFAULT_INPUT) -> int:
    passports = []
    with open(loc) as f:
        passports_raw = ''.join(f.readlines()).split('\n\n')
        for ps in passports_raw:
            ps = ' '.join(ps.split('\n')).split(' ')
            passport = {(f := field.split(':'))[0]: f[1] for field in ps}
            passports.append(passport)
    part_1 = sum(1
                 for passport in passports
                 if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport))
    part_2 = sum(1 for passport in passports if is_valid(passport))
    return part_1, part_2

def is_valid(passport: dict[str, str]) -> bool:
    if any(val not in passport for val in ('byr', 'iyr', 'eyr', 'hgt',
                                           'hcl', 'ecl', 'pid')):
        return False
    
    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False

    if m := re.fullmatch(r'(\d+)(cm|in)', passport['hgt']):
        size = int(m.group(1))
        units = m.group(2)
        if units == 'cm' and not (150 <= size <= 193):
            return False
        if units == 'in' and not (59 <= size <= 76):
            return False
    else:
        return False

    if not re.fullmatch(r'#[0-9a-f]{6}', passport['hcl']):
        return False
    
    if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry',
                               'grn', 'hzl', 'oth'):
        return False

    if not re.fullmatch(r'\d{9}', passport['pid']):
        return False
    
    return True
    
                    

if __name__ == '__main__':
    part_1, part_2 = day_4()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
