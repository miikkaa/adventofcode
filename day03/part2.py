lines = []
with open('input.txt', encoding="utf-8") as input:
  for line in input:
      lines.append(line.strip())

def flush(buffer, row_ix, col_ixs, numbers):
  if len(buffer) > 0: numbers.append((row_ix, col_ixs, int(buffer)))

def get_numbers(lines):
  numbers = []
  for row_ix, line in enumerate(lines):
    buffer = ''
    col_from_ix = -1
    
    for col_ix, char in enumerate(line):
      if char.isnumeric():
        buffer += char
        # start recording index
        if col_from_ix == -1: col_from_ix = col_ix
      
      flush_at_ix = -1
      should_flush = False
      # flush if first non-numeric or if end of line
      if not char.isnumeric():
        should_flush = True
        flush_at_ix = col_ix - 1
      elif col_ix == (len(line) - 1):
        should_flush = True
        flush_at_ix = col_ix

      if should_flush:
        flush(buffer, row_ix, (col_from_ix, flush_at_ix), numbers)
        buffer = ''
        col_from_ix = -1

  return numbers

def get_coords_with_stars(lines, row_ix, col_ix_range, num, all_coords_with_stars):
  coords_to_check = []
  col_ix_full_range = range(max(0, col_ix_range[0] - 1), min(len(lines[row_ix]) - 1, col_ix_range[1] + 1) + 1)

  if row_ix > 0:
    for col_ix in col_ix_full_range:
      coords_to_check.append((row_ix - 1, col_ix))
    
  if row_ix < len(lines) - 1:
    for col_ix in col_ix_full_range:
      coords_to_check.append((row_ix + 1, col_ix))
    
  if col_ix_range[0] > 0:
    coords_to_check.append((row_ix, col_ix_full_range[0]))
  if col_ix_range[1] < len(lines[row_ix]) - 1:
    coords_to_check.append((row_ix, col_ix_full_range[-1]))

  for row, col in coords_to_check:
    if lines[row][col] == '*':
      if (row, col) not in all_coords_with_stars: all_coords_with_stars[(row, col)] = [num]
      else: all_coords_with_stars[(row, col)].append(num)
  pass

def get_all_coords_with_stars(numbers):
  all_coords_with_stars = {}
  for number in numbers:
    row_ix = number[0]
    col_ixs = number[1]
    num = number[2]
    get_coords_with_stars(lines, row_ix, col_ixs, num, all_coords_with_stars)

  return all_coords_with_stars

def get_gears_sum(all_coords_with_stars):
  gears_sum = 0
  for (coords, numbers) in all_coords_with_stars.items():
    if len(numbers) == 2:
      gears_sum += numbers[0] * numbers[1]
  
  return gears_sum

numbers = get_numbers(lines)
all_coords_with_stars = get_all_coords_with_stars(numbers)

print(get_gears_sum(all_coords_with_stars))


      