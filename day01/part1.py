lines = []
with open('input.txt', encoding="utf-8") as input:
    for line in input:
        lines.append(line.strip())

numbers = []
for line in lines:
    num1, num2 = None, None

    for i in range(len(line)):
        ix1 = line[i]
        ix2 = line[-i - 1]

        if num1 is None:
            num1 = ix1 if ix1.isnumeric() else None
        if num2 is None:
            num2 = ix2 if ix2.isnumeric() else None

    numbers.append(int(num1 + num2))

print(f"result = {sum(numbers)}")
