lines = []
file = 'input.txt'
# file = 'input_test1.txt'
# file = 'input_test2.txt'
with open(file, encoding="utf-8") as input:
    for line in input:
        lines.append(line.strip())

spelled_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

numbers = []
for line in lines:
    numbers_in_line = []
    i = 0

    while i < len(line):
        char = line[i]

        if char.isnumeric():
            number = int(char)
            numbers_in_line.append(number)
        else:
            rest_of_string = line[i:]

            for key in spelled_numbers.keys():
                if rest_of_string.startswith(key):
                    number = spelled_numbers[key]
                    numbers_in_line.append(number)
                    break

        i += 1

    num1 = numbers_in_line[0]
    num2 = numbers_in_line[-1]

    numbers.append((num1 * 10) + num2)

print(f"result = {sum(numbers)}")
