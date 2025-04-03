def read_file(filename):
    left= []
    right = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.split('   ')
            left.append(int(line[0]))
            right.append(int(line[1]))

    return left, right

def get_total_distance():
    res = 0
    left, right = read_file('input')

    for i, j in zip(sorted(left), sorted(right)):
        res += abs(i - j)

    return res

def get_the_similarity_score():
    res = 0
    left, right = read_file('input')

    for i, j in zip(sorted(left), sorted(right)):
        res += (left.count(i) * abs(i))

    return res

print(get_total_distance(), get_the_similarity_score())