import sys
from functools import cmp_to_key
from more_itertools import split_at


def is_correct_update(update, rules):
    return all(0 < update.find(rule[1]) >= update.find(rule[0])
               or update.find(rule[1]) < 0
               or update.find(rule[0]) < 0 for rule in rules)


rules_tmp, updates = tuple(split_at([line.strip() for line in open("day5/data.txt", "r").readlines()], lambda cr: cr == ''))
rules = {tuple(key.split('|')) for key in rules_tmp}


def part1():
    correct_updates = [update.split(',') for update in updates if is_correct_update(update, rules)]
    return sum([int(correct_update[len(correct_update)//2]) for correct_update in correct_updates])


def part2():
    incorrect_updates = [sorted(update.split(','), key=cmp_to_key(lambda u1, u2: -1 if (u1, u2) in rules else 1))
                         for update in updates if not is_correct_update(update, rules)]
    return sum([int(correct_update[len(correct_update)//2]) for correct_update in incorrect_updates])

