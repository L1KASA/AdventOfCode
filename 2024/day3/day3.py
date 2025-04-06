import re

def read_file():
    list_1 = list()

    with open('input', 'r') as file:
        for line in file:
            list_1.append(line)
    return list_1

def part1():
    list_1 = read_file()
    pattern = r"mul\((\d{0,3}),(\d{0,3})\)"

    matches = [re.findall(pattern, text) for text in list_1]
    res = 0
    for sublist in matches:
        for x, y in sublist:
            res+=int(x)*int(y)

    return res

def part2():
    list_1 = read_file()
    pattern = r"(do\(\)|don't\(\))|mul\((\d{0,3}),(\d{0,3})\)"
    matches = [re.findall(pattern, test) for test in list_1]
    res = 0
    enabled = True
    for sublist in matches:
        for x, y, z in sublist:
            if x == "don't()":
                enabled = False
            elif x == "do()":
                enabled = True
            elif y and z and enabled:
                res+=int(y)*int(z)

    return res

print(part2())