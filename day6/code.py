from collections import deque
from itertools import count


def find_guard_initial_position(lab_area):
    idx_guard = (''.join(lab_area).index('^'))
    y = idx_guard // len(lab_area)
    x = idx_guard - y * len(lab_area)
    return x, y


def there_is_an_obstacle_forward(x, y, direction, lab_area):
    return (direction == 'up' and lab_area[y-1][x] in {'#', 'o'}
            or direction == 'right' and lab_area[y][x+1] in {'#', 'o'}
            or direction == 'down' and lab_area[y+1][x] in {'#', 'o'}
            or direction == 'left' and lab_area[y][x-1] in {'#', 'o'})


def move_forward(x, y, direction):
    if direction == 'up':
        return x, y-1
    elif direction == 'right':
        return x+1, y,
    elif direction == 'down':
        return x, y+1
    elif direction == 'left':
        return x-1, y


def guard_is_still_in_lab(x, y, lab_area):
    return 0 < y < len(lab_area)-1 and 0 < x < len(lab_area[0])-1


def replace_element_at(lab_area, x, y, value):
    lab_area[y] = lab_area[y][:x] + value + lab_area[y][x + 1:]


def part1():
    lab_area = [line.strip() for line in open("day6/data.txt", "r").readlines()]

    # Setup
    directions = deque(['up', 'right', 'down', 'left'])
    guard_x, guard_y = find_guard_initial_position(lab_area)
    guard_direction = directions[0]
    visited = dict()
    visited[(guard_x, guard_y)] = 1

    while guard_is_still_in_lab(guard_x, guard_y, lab_area):

        # Walk and record positions
        if there_is_an_obstacle_forward(guard_x, guard_y, guard_direction, lab_area):
            directions.rotate(-1)
            guard_direction = directions[0]

        else:
            guard_x, guard_y = move_forward(guard_x, guard_y, guard_direction)
            position = (guard_x, guard_y)
            if position not in visited:
                visited[position] = 1
            if not guard_is_still_in_lab(guard_x, guard_y, lab_area):
                return len(visited)


def part2():
    lab_area = [line.strip() for line in open("day6/data.txt", "r").readlines()]
    blocking_positions_bruteforce_list = [(x, y) for y in range(len(lab_area)) for x in range(len(lab_area[0]))]
    blocking_positions = []

    for retroencabulator_x, retroencabulator_y in blocking_positions_bruteforce_list:

        # Setup
        directions = deque(['up', 'right', 'down', 'left'])
        guard_direction = directions[0]
        guard_x, guard_y = find_guard_initial_position(lab_area)
        visited = dict()
        visited[(guard_x, guard_y, guard_direction)] = 1

        # It makes no sens to override an existing blocking stuff
        if lab_area[retroencabulator_y][retroencabulator_x] in {'#', '^'}:
            continue

        # Add a blocking stuff to make guard gogoliser
        replaced_element = lab_area[retroencabulator_y][retroencabulator_x]
        replace_element_at(lab_area, retroencabulator_x, retroencabulator_y, 'o')

        is_guard_blocked = False
        while not is_guard_blocked or guard_is_still_in_lab(guard_x, guard_y, lab_area):
            # Walk and record positions
            if guard_is_still_in_lab(guard_x, guard_y, lab_area):
                if there_is_an_obstacle_forward(guard_x, guard_y, guard_direction, lab_area):
                    directions.rotate(-1)
                    guard_direction = directions[0]
                else:
                    guard_x, guard_y = move_forward(guard_x, guard_y, guard_direction)
                    position = (guard_x, guard_y, directions[0])

                    if position not in visited:
                        visited[position] = 0
                    visited[position] += 1

                    if visited[position] > 1:
                        is_guard_blocked = True
                        break
            else:
                break
        if is_guard_blocked:
            blocking_positions.append((retroencabulator_x, retroencabulator_y))

        # Removing a blocking stuff
        replace_element_at(lab_area, retroencabulator_x, retroencabulator_y, replaced_element)
    print(len(blocking_positions))
    return len(blocking_positions)
