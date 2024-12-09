from itertools import groupby


def expand_from_allocation_table(allocation_table):
    return ''.join([str(f_or_s[0]//2) * int(f_or_s[1]) if f_or_s[0] % 2 == 0 else '.' * int(f_or_s[1]) for f_or_s in enumerate(allocation_table)])

def defragment_disk(expanded_data):
    print(expanded_data)
    for idx_right, char_right in reversed(list(enumerate(expanded_data))):
        idx_left = expanded_data.find('.', len(expanded_data) - idx_right-1)
        char_left = expanded_data[idx_left]

        if (idx_right <= idx_left):
            print(expanded_data)
            return expanded_data

        expanded_data = swap(expanded_data, idx_left, idx_right)
    
    return expanded_data

def compute_checksum(data):
    print(data)
    print(sum([idx * int(char) for idx, char in enumerate(data[:data.find('.')])]))
    return 0

def split_on_diff(string):
    return [''.join(group) for _, group in groupby(string)]

def swap(s, i, j):
    return ''.join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]))

def part1():
    allocation_table = open("day9/sample.txt", "r").read()
    defragmented_data = defragment_disk(expand_from_allocation_table(allocation_table))
    return compute_checksum(defragmented_data)

    

    print(defragmented_data)
    return 0

def part2():
    allocation_table = open("day9/sample.txt", "r").read()
    return 0