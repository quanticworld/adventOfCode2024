from collections import deque
from functools import lru_cache


# Ouaiiii ouaiiii c'est limite limite, mais ça sert à ça, la memoisation hein !
@lru_cache(None)
def calc_next(value, current_iter, max_iter, accu):
    if current_iter == max_iter:
        return 1

    if value == 0:
        return calc_next(1, current_iter + 1, max_iter, accu)
    elif len(str(value)) % 2 == 0:
        str_value = str(value)
        return (calc_next(int(str_value[:len(str_value) // 2]), current_iter + 1, max_iter, accu)
                + calc_next(int(str_value[len(str_value) // 2:]), current_iter + 1, max_iter, accu))
    else:
        return calc_next(value * 2024, current_iter + 1, max_iter, accu + 1)


def solve(iterations):
    stones = deque([int(stone) for stone in open("day11/sample.txt", "r").read().split(' ')])
    return sum(list(map(lambda value: calc_next(value, 0, iterations, 0), stones)))


def part1():
    result = solve(25)
    return result


def part2():
    result = solve(75)
    return result
