from collections import defaultdict


def expand_from_allocation_table(allocation_table):
    result = defaultdict(list)
    current_insert_index = 0
    for idx, value in enumerate(allocation_table):
        if int(value) > 0:
            if idx % 2 == 0:
                for i in range(int(value)):
                    result[idx // 2].append(current_insert_index)
                    current_insert_index += 1
            else:
                for i in range(int(value)):
                    result[-1].append(current_insert_index)
                    current_insert_index += 1
    return result


def defragment_disk(expanded_data):
    idx_space = 0
    for key in list(reversed(expanded_data.keys())):
        if key == -1:
            continue
        for idx in reversed(range(len(expanded_data[key]))):
            if expanded_data[key][idx] > expanded_data[-1][idx_space]:
                swap_last_value_with_first_space(expanded_data[key], expanded_data[-1], idx, idx_space)
            else:
                return expanded_data
            idx_space += 1


def defragment_disk_part2(expanded_data):
    empty_space_already_taken = set()
    for key in list(reversed(expanded_data.keys())):
        if key == -1:
            continue

        replacement_start_idx = find_first_continuous_space_of_size(expanded_data[-1], len(expanded_data[key]),
                                                                    expanded_data[key][-1], empty_space_already_taken)

        if replacement_start_idx >= 0:
            for idx in range(len(expanded_data[key])):
                swap_last_value_with_first_space(expanded_data[key], expanded_data[-1], idx, replacement_start_idx)
                empty_space_already_taken.add(replacement_start_idx)
                replacement_start_idx += 1

    return expanded_data


def find_first_continuous_space_of_size(indices, length, max_idx, empty_space_already_taken):
    if length == 1:
        for idx in range(len(indices)):
            if indices[idx] < max_idx and not idx in empty_space_already_taken:
                return idx
    else:
        for i in range(len(indices) - length + 1):
            if indices[i] >= max_idx or i in empty_space_already_taken:
                continue

            is_sequence = True
            for j in range(1, length):
                if indices[i + j - 1] != indices[i + j] - 1:
                    is_sequence = False
                    break

            if is_sequence:
                return i

    return -1


def compute_checksum(data):
    return sum(key * value for key, values in data.items() if key != -1 for value in values)


def swap_last_value_with_first_space(value_positions, space_positions, idx, idx_space):
    value_positions[idx], space_positions[idx_space] = space_positions[idx_space], value_positions[idx]


def part1():
    allocation_table = open("day9/sample.txt", "r").read()
    defragmented_data = defragment_disk(expand_from_allocation_table(allocation_table))
    return compute_checksum(defragmented_data)


def part2():
    allocation_table = open("day9/sample.txt", "r").read()
    defragmented_data = defragment_disk_part2(expand_from_allocation_table(allocation_table))
    result = compute_checksum(defragmented_data)
    return result