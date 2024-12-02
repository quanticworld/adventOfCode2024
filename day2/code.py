import itertools


def part1():
    reports = [[int(e) for e in row.split(' ')] for row in open("day2/data1.txt", "r").readlines()]
    safe_reports_inc = list(
        filter(lambda r: all(r[i] < r[i + 1] and abs(r[i] - r[i + 1]) <= 3 for i in range(len(r) - 1)), reports))
    safe_reports_dec = list(
        filter(lambda r: all(r[i] > r[i + 1] and abs(r[i] - r[i + 1]) <= 3 for i in range(len(r) - 1)), reports))

    return len(safe_reports_inc + safe_reports_dec)


def part2():
    reports = [[int(e) for e in row.split(' ')] for row in open("day2/data2.txt", "r").readlines()]
    is_sorted_strict = lambda r: all(r[i] < r[i + 1] and abs(r[i] - r[i + 1]) <= 3 for i in range(len(r) - 1))
    is_reverse_sorted_strict = lambda r: all(r[i] > r[i + 1] and abs(r[i] - r[i + 1]) <= 3 for i in range(len(r) - 1))
    is_barely_safe = lambda r: sum([is_sorted_strict(sub_r) or is_reverse_sorted_strict(sub_r) for sub_r in
                                    list(itertools.combinations(r, len(r) - 1))]) > 0
    return len(list(filter(lambda r: is_sorted_strict(r) or is_reverse_sorted_strict(r) or is_barely_safe(r), reports)))
