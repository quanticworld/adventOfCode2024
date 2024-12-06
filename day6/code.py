from collections import deque


def find_guard_initial_position(lab_area):
    idx_guard = (''.join(lab_area).index('^'))
    y = idx_guard // len(lab_area)
    x = idx_guard - y * len(lab_area)
    return x, y


def there_is_an_obstacle_forward(x, y, direction, lab_area):
    return (direction == 'up' and lab_area[y-1][x] == '#'
            or direction == 'right' and lab_area[y][x+1] == '#'
            or direction == 'down' and lab_area[y+1][x] == '#'
            or direction == 'left' and lab_area[y][x-1] == '#')


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


def part1():
    lab_area = [line.strip() for line in open("day6/data.txt", "r").readlines()]

    # Setup
    directions = deque(['up', 'right', 'down', 'left'])
    guard_x, guard_y = find_guard_initial_position(lab_area)
    guard_direction = directions[0]
    visited = dict()
    visited[(guard_x, guard_y)] = True

    while guard_is_still_in_lab(guard_x, guard_y, lab_area):

        # Walk and record positions
        while there_is_an_obstacle_forward(guard_x, guard_y, guard_direction, lab_area):
            directions.rotate(-1)
            guard_direction = directions[0]

        while not there_is_an_obstacle_forward(guard_x, guard_y, guard_direction, lab_area):
            guard_x, guard_y = move_forward(guard_x, guard_y, guard_direction)
            position = (guard_x, guard_y)
            if position not in visited:
                visited[position] = True
            if not guard_is_still_in_lab(guard_x, guard_y, lab_area):
                return len(visited)


def part2():
    return 2
