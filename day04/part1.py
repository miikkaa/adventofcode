import re

lines = []
with open('input.txt', encoding="utf-8") as input:
  lines = input.read().strip().split('\n')

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
line_exp = re.compile('Card(.+)\: (.+) \| (.+)')

cards = []

def handle_num_list(nums):
  return list(
    map(lambda v: int(v), list(
      filter(lambda v: v != '', nums))
    )
  )

def intersect(list1, list2):
  intersection = []
  for el in list1:
    if el in list2: intersection.append(el)
  return intersection

sum = 0
for line in lines:
  matches = line_exp.match(line)
  winning = handle_num_list(matches.group(2).split(' '))
  numbers = handle_num_list(matches.group(3).split(' '))
  no_of_matches = len(intersect(winning, numbers))
  sum += 2 ** (no_of_matches - 1) if no_of_matches > 0 else 0

print(sum)