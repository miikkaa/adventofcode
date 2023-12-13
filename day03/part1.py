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
    col_ix = -1
    
    for col_ix, char in enumerate(line):
      if char.isnumeric():
        buffer += char
        # start recording index
        if col_from_ix == -1: col_from_ix = col_ix
      else:
        # flush inside a line
        flush(buffer, row_ix, (col_from_ix, col_ix - 1), numbers)
        buffer = ''
        col_from_ix = -1
    
    # flush if at the end of a line
    flush(buffer, row_ix, (col_from_ix, col_ix), numbers)

  return numbers

def check_neighbours(lines, row_ix, col_ix_range):
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
    if lines[row][col] != '.':
      return True

  return False

def get_numbers_with_adjacent_symbols(numbers):
  numbers_with_adjacent_symbols = []
  for number in numbers:
    row_ix = number[0]
    col_ixs = number[1]
    num = number[2]
    if check_neighbours(lines, row_ix, col_ixs):
      numbers_with_adjacent_symbols.append(num)

  return numbers_with_adjacent_symbols

numbers = get_numbers(lines)
numbers_with_adjacent_symbols = get_numbers_with_adjacent_symbols(numbers)

print(sum(numbers_with_adjacent_symbols))


      