import itertools
from collections import defaultdict

IGNORE_CHAR_LIST = ['.', '#']


def get_positions_by_symbol(data):
    positions = defaultdict(lambda: defaultdict(int))

    for j, row in enumerate(data):
        for i, symbol in enumerate(row):
            if symbol not in IGNORE_CHAR_LIST:
                positions[symbol][(i, j)] += 1
    return positions


def is_inbound(antinode, data):
    return (0 <= antinode[0] < len(data[0])
            and 0 <= antinode[1] < len(data))


def solve(data, signal_strength):

    positions_by_symbol = get_positions_by_symbol(data)
    antinodes = [[0] * len(data[0]) for _ in range(len(data))]

    for symbol in positions_by_symbol.keys():
        couples = list(itertools.combinations(positions_by_symbol[symbol].keys(), 2))

        # Compute positions that should be an antipod by subtracting/adding the x and y difference between 2 positions
        # There are 4 cases : p1 is on top-left from p2, top-right, bottom-left or bottom-right
        for couple in couples:
            x_diff = x_step = abs(couple[0][0] - couple[1][0])
            y_diff = y_step = abs(couple[0][1] - couple[1][1])
            x1, y1, x2, y2 = couple[0][0], couple[0][1], couple[1][0], couple[1][1]

            for strgh in range(signal_strength):
                antinode1 = (-1, -1)
                antinode2 = (-1, -1)

                p1_p2_direction_to_new_antinode_coordinates = {
                    (True, True): [(x1 - x_diff, y1 - y_diff), (x2 + x_diff, y2 + y_diff)],
                    (False, True): [(x1 + x_diff, y1 - y_diff), (x2 - x_diff, y2 + y_diff)],
                    (True, False): [(x1 - x_diff, y1 + y_diff), (x2 + x_diff, y2 - y_diff)],
                    (False, False): [(x2 - x_diff, y2 - y_diff), (x1 + x_diff, y1 + y_diff)]
                }

                key = (x1 < x2, y1 < y2)
                antinode1, antinode2 = p1_p2_direction_to_new_antinode_coordinates[key]

                for antinode in [antinode1, antinode2]:
                    if is_inbound(antinode, data):
                        antinodes[antinode[1]][antinode[0]] += 1

                x_diff += x_step
                y_diff += y_step

    return antinodes, positions_by_symbol


def part1():
    data = [row for row in open("day8/sample.txt", "r").read().splitlines()]
    antinodes, _ = solve(data, signal_strength=1)
    return sum([sum(1 for v in node if v != 0) for node in antinodes])


def part2():
    data = [row for row in open("day8/sample.txt", "r").read().splitlines()]
    antinodes, positions_by_symbol = solve(data, signal_strength=len(data) * 2)

    for x, y in itertools.chain.from_iterable(positions_by_symbol.values()):
        antinodes[y][x] += 1

    return sum([sum(1 for v in node if v != 0) for node in antinodes])
