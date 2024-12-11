from collections import defaultdict, deque
from pprint import pprint


def solve(iterations):
    stones = deque([int(stone) for stone in open("day11/sample.txt", "r").read().split(' ')])

    for i in range(iterations):
        new_stones = deque()
        for stone_idx in range(len(stones)):

            if stones[stone_idx] == 0:
                new_stones.append(1)

            elif len(str(stones[stone_idx])) % 2 == 0:
                str_stone = str(stones[stone_idx])
                first_stone = int(str_stone[:len(str_stone) // 2])
                second_stone = int(str_stone[len(str_stone) // 2:])
                new_stones.append(second_stone)
                new_stones.append(first_stone)

            else:
                new_stones.append(stones[stone_idx] * 2024)
        stones = new_stones
        a = 1
    return len(stones)


def part1():
    return solve(25)

def part2():
    return solve(75)
