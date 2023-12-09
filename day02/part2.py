import re
from functools import reduce

lines = []
with open('input.txt', encoding="utf-8") as input:
    for line in input:
        lines.append(line.strip())

game_regexp = re.compile('Game (\d+)\: (.+)')
set_regexp = re.compile('(\d+) (blue|red|green)')
set_delimiter = ';'
numbers = []

empty_set = {
    'red': 1,
    'green': 1,
    'blue': 1
}

def multiply(results: dict):
    product = 1
    for num in results.values():
        product *= num
    return product

for line in lines:
    # game
    # Game ID: SET1; SET2; SET3; ...
    game_id_with_sets = game_regexp.match(line)
    game_id = int(game_id_with_sets.group(1))
    # [ '3 blue, 2 red', '1 green, 3 green', etc. ]
    game_sets = game_id_with_sets.group(2).split(set_delimiter)
    game_possible = True

    set_fewest_num = empty_set.copy()

    for set in game_sets:
        # individual set
        # e.g '3 blue, 2 red'

        for (number, color) in re.findall(set_regexp, set):
            set_fewest_num[color] = max(int(number), set_fewest_num[color])

    numbers.append(multiply(set_fewest_num))

print(f"result = {sum(numbers)}")