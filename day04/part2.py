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

def intersection(list1, list2):
  intersection = []
  for el in list1:
    if el in list2: intersection.append(el)
  return intersection

visits = {}
scratchcards = 0

for row_ix, line in enumerate(lines):
  visits[row_ix] = 0

for row_ix, line in enumerate(lines):
  visits[row_ix] += 1
  
  matches = line_exp.match(line)
  winning = handle_num_list(matches.group(2).split(' '))
  numbers = handle_num_list(matches.group(3).split(' '))
  no_of_matches = len(intersection(winning, numbers))

  if no_of_matches > 0:
    for i in range(1, no_of_matches + 1):
      visits[row_ix + i] += visits[row_ix]

for (_, numbers) in visits.items():
  scratchcards += numbers

print(scratchcards)