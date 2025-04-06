def read_file():
    list_1 = list()
    with open('input', 'r') as file:
        list_1 = [[int(x) for x in line.split()] for line in file]
    return list_1
   

def is_safe(row):
    decrease = 0
    increase = 0
    for j in range(len(row) - 1):
        r = abs(row[j] - row[j + 1])
        if (r == 0) or (r > 3):
            return False
        if row[j] > row[j + 1]:
            decrease += 1
        else:
            increase += 1
        if decrease > 0 and increase > 0:
            return False
    return True

def part1():
    list_1 = read_file()
    unsafe = list() # Все небезопасные отчеты
    res = 0 # Сколько отчетов небезопасны
    for row in list_1:
        if not is_safe(row):
            res+=1
            unsafe.append(row)
    return len(list_1)-res, unsafe

def part2():
    res_of_part1, unsafe = part1()
    saved_reports = 0

    for row in unsafe:
        for i in range(len(row)):
            temp_row = row[:i] + row[i+1:]
            if is_safe(temp_row):
                saved_reports += 1
                break

    return saved_reports + res_of_part1

print(part2())
