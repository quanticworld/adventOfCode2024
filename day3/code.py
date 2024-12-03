import re
from functools import reduce
from operator import mul


def part1():
    sequence = open("day3/data.txt", "r").read().replace('\n', '')
    return sum([reduce(mul, (tuple(map(int, couple))), 1) for couple in re.findall('mul\\(([0-9]+),([0-9]+)\\)', sequence)])


def part2():
    sequence = open("day3/data.txt", "r").read().replace('\n', '')
    clean_sequence = re.sub('(don\'t\\(\\)).*?(do\\(\\)|$)', '', sequence)
    return sum([reduce(mul, (tuple(map(int, couple))), 1) for couple in re.findall('mul\\(([0-9]+),([0-9]+)\\)', clean_sequence)])
