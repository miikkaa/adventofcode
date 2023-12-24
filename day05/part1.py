import re

lines = []
with open('test01.txt', encoding="utf-8") as input:
  lines = input.read().strip().split('\n')

# Pattern for "destination-to-source map:"
source_to_destination_exp = re.compile('^([a-z]+)-to-([a-z]+) map\:$')
# <dest range start> <source range start> <range length>
line_exp = re.compile('^(\d+)\s+(\d+)\s+(\d+)$')
locations = []

def find_location():
  seeds_exp = re.compile('^seeds: (.+)$')
  seeds = list(map(lambda v: int(v), seeds_exp.match(lines[0]).group(1).split(' ')))
  del lines[0]

  for seed in seeds:
    print(f"\nseed = {seed}")
    ignore_rest_of_category = True
    coord = seed

    for line in lines:
      # print(f"line = <{line}>")
      category_match = source_to_destination_exp.match(line)
      
      if category_match is not None:
        # if not ignore_rest_of_category: print(f"->{coord}")
        # new category found
        ignore_rest_of_category = False
        # print(f"category = {category_match.group(2)}")

      elif len(line) > 0 and not ignore_rest_of_category:
        # inside a category
        range_match = line_exp.match(line)
        range_length = int(range_match.group(3))
        dest_range_start = int(range_match.group(1))
        src_range_start = int(range_match.group(2))

        # print(f"checking if seed {seed} inside [{src_range_start}, {src_range_start + range_length}]")
        
        if src_range_start <= coord <= src_range_start + range_length:
          coord = coord - src_range_start + dest_range_start
          # print(f"YES, will skip the rest... => {coord}")
          # print(f"->{coord}")
          ignore_rest_of_category = True
    
    # print(f"loc = {coord}")
    locations.append(coord)
  
  print(min(locations))

find_location()
