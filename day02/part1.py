import re

lines = []
with open('input.txt', encoding="utf-8") as input:
    for line in input:
        lines.append(line.strip())

game_regexp = re.compile('Game (\d+)\: (.+)')
set_regexp = re.compile('(\d+) (blue|red|green)')
set_delimiter = ';'
possible_games = []

thresholds = {
    'red': 12,
    'green': 13,
    'blue': 14
}

empty_set = {
    'red': 0,
    'green': 0,
    'blue': 0
}

def set_results_impossible(results: dict, thresholds = thresholds):
    return True \
        if results['red'] > thresholds['red']\
            or results['blue'] > thresholds['blue']\
            or results['green'] > thresholds['green']\
        else False

for line in lines:
    # game
    # Game ID: SET1; SET2; SET3; ...
    game_id_with_sets = game_regexp.match(line)
    game_id = int(game_id_with_sets.group(1))
    # [ '3 blue, 2 red', '1 green, 3 green', etc. ]
    game_sets = game_id_with_sets.group(2).split(set_delimiter)
    game_possible = True

    for set in game_sets:
        # individual set
        # e.g '3 blue, 2 red'
        set_results = empty_set.copy()

        for (number, color) in re.findall(set_regexp, set):
            set_results[color] = int(number)

        if set_results_impossible(set_results):
            game_possible = False
            break

    if game_possible: possible_games.append(game_id)

print(f"result = {sum(possible_games)}")