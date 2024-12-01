from collections import Counter


def part1():
    l1, l2 = map(list, zip(*[row.split('   ') for row in open("day1/data1.txt", "r").readlines()]))
    l1.sort(), l2.sort()
    return sum([abs(int(e1)-int(e2)) for e1, e2 in zip(l1, l2)])


def part2():
    l1, l2 = map(list, zip(*[row.split('   ') for row in open("day1/data2.txt", "r").readlines()]))
    l1 = [int(e) for e in l1]
    l2 = [int(e) for e in l2]
    l_dict = Counter(l2)

    return sum(e * l_dict[e] for e in l1 if e in l_dict)
