DEFAULT_INPUT = 'day21.txt'

def day_21(loc: str = DEFAULT_INPUT) -> tuple[int, str]:
    ingredients = []
    allergens = {}
    with open(loc) as f:
        for line in f.readlines():
            line = line.rstrip(')\n')
            ings, allers = line.split(' (contains ')
            ings = ings.split(' ')
            allers = allers.split(', ')
            for ingredient in ings:
                ingredients.append(ingredient)
            for allergen in allers:
                if allergen not in allergens:
                    allergens[allergen] = set(ings)
                else:
                    allergens[allergen] &= set(ings)
    non_allergens = set(ingredients)
    for k, v in allergens.items():
        non_allergens -= v
    allergens = solve_allergens(allergens)
    allergen_list = list(allergens.items())
    allergen_list.sort(key = lambda t:t[0])
    return sum(1 for ing in ingredients if ing in non_allergens), \
           ','.join(t[1] for t in allergen_list)

def solve_allergens(allergens: dict[str, set[str]]) -> dict[str, str]:
    solved = set()
    while any(isinstance(value, set) for value in allergens.values()):
        for key, value in allergens.items():
            if isinstance(value, set):
                value -= solved
                if len(value) == 1:
                    new_value = list(value)[0]
                    allergens[key] = new_value
                    solved.add(new_value)
    return allergens
    

if __name__ == '__main__':
    part_1, part_2 = day_21()
    print('Solution for Part One:', part_1)
    print('Solution for Part Two:', part_2)
