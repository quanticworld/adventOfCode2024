from collections import defaultdict, deque


def solve(take_all_ratings):
    data = [[int(col) for col in row] for row in open("day10/data.txt", "r").read().splitlines()]
    # Build dict of neighbours for each position
    nearby_positions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    trailheads = defaultdict(int)

    for y, row in enumerate(data):
        for x, _ in enumerate(row):
            if data[y][x] != 9:
                continue

            coordinates_to_visite = deque([(x, y)])
            visited = set()

            while len(coordinates_to_visite) > 0:
                curr_x, curr_y = coordinates_to_visite.popleft()

                if (curr_x, curr_y) in visited:
                    continue
                if not take_all_ratings:
                    visited.add((curr_x, curr_y))

                for dx, dy in nearby_positions:
                    next_pos_x = curr_x + dx
                    next_pos_y = curr_y + dy
                    if ((0 <= next_pos_y < len(data))
                            and (0 <= next_pos_x < len(data[0]))):
                        if data[next_pos_y][next_pos_x] == data[curr_y][curr_x] - 1:
                            coordinates_to_visite.append((next_pos_x, next_pos_y))

                if data[curr_y][curr_x] == 0:
                    trailheads[(x, y)] += 1

    return sum(trailheads.values())


def part1():
    return solve(take_all_ratings=False)

def part2():
    return solve(take_all_ratings=True)
