from itertools import chain, groupby
import numpy

def expand_from_allocation_table(allocation_table, flatten):
    parsed_list = [[f_or_s[0]//2] * int(f_or_s[1]) if f_or_s[0] % 2 == 0 else [-1] * int(f_or_s[1]) for f_or_s in enumerate(allocation_table)]
    if flatten:
        return numpy.array(list(chain.from_iterable(parsed_list)))
    else:
        return numpy.array(parsed_list, dtype="object")
        
def np_index(array, value):
    return numpy.where(array == value)[0][0]

def np_list_index(array, value, min_value_length = -1):
    if min_value_length > 0:
        lengths = numpy.array([len(sublist) for sublist in array])
        return numpy.where(lengths == min_value_length)
    else:
        return list(filter(lambda l: len(l) > 0, [(idx, sublist) if all(x == value and x == sublist[0] for x in sublist) else [] for idx, sublist in enumerate(array)]))[0][0]

def defragment_disk(expanded_data):
    last_index_of_empty_space = len(expanded_data) - 1 - np_index(expanded_data, -1)
    for idx_right, _ in reversed(list(enumerate(expanded_data))):
        remaining_spaces = -1 in expanded_data
        if not remaining_spaces:
            return expanded_data
        idx_left = np_index(expanded_data, -1)
        swap_and_replace_right(expanded_data, idx_left, idx_right, -2)
    
def defragment_disk_part2(expanded_data):
    last_index_of_empty_space = len(expanded_data) - 1 - np_list_index(expanded_data[::-1], -1)
    for idx_right, value_right in reversed(list(enumerate(expanded_data))):
        remaining_spaces = np_list_index(expanded_data[::-1], -1) >= 0
        if not remaining_spaces:
            return expanded_data
        idx_left = np_list_index(expanded_data, -1)
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
    allocation_table = open("day9/sample.txt", "r").read()
    defragmented_data = defragment_disk(expand_from_allocation_table(allocation_table, flatten=True))
    return compute_checksum(defragmented_data)

def part2():
    allocation_table = open("day9/sample.txt", "r").read()
    defragmented_data = defragment_disk_part2(expand_from_allocation_table(allocation_table, flatten=False))
    return compute_checksum(defragmented_data)
