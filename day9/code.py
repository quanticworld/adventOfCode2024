from itertools import chain, groupby

import numpy


def expand_from_allocation_table(allocation_table):
    result = numpy.array(list(chain.from_iterable([[f_or_s[0]//2] * int(f_or_s[1]) if f_or_s[0] % 2 == 0 else [-1] * int(f_or_s[1]) for f_or_s in enumerate(allocation_table)])))
    return result

def np_index(array, value):
    return numpy.where(array == value)[0][0]

def defragment_disk(expanded_data):
    last_index_of_empty_space = len(expanded_data) - 1 - np_index(expanded_data[::-1], -1)
    for idx_right, _ in reversed(list(enumerate(expanded_data))):
        remaining_spaces = -1 in expanded_data

        if not remaining_spaces:
            return expanded_data

        idx_left = np_index(expanded_data, -1)


        swap_and_replace_right(expanded_data, idx_left, idx_right, -2)
    
    return expanded_data

def compute_checksum(data):
    return sum([idx * value for idx, value in enumerate(data[:np_index(data, -2)])])


def group_repeated_values(data):
    return  [list(group) for _, group in groupby(data)]

def swap_and_replace_right(data, i, j, replace_value):
    data[i] = data[j]
    data[j] = replace_value

def part1():
    allocation_table = open("day9/data.txt", "r").read()
    defragmented_data = defragment_disk(expand_from_allocation_table(allocation_table))
    return compute_checksum(defragmented_data)

    

    print(defragmented_data)
    return 0

def part2():
    allocation_table = open("day9/sample.txt", "r").read()
    return 0