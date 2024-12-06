import timeit
from day1.code import part1 as d1_1, part2 as d1_2
from day2.code import part1 as d2_1, part2 as d2_2
from day3.code import part1 as d3_1, part2 as d3_2
from day4.code import part1 as d4_1, part2 as d4_2
from day5.code import part1 as d5_1, part2 as d5_2
from day6.code import part1 as d6_1, part2 as d6_2

if __name__ == '__main__':
    num_runs = 1
    # day1_1_time = timeit.Timer(d1_1).timeit(num_runs) / num_runs * 1000
    # day1_2_time = timeit.Timer(d1_2).timeit(num_runs) / num_runs * 1000
    # day2_1_time = timeit.Timer(d2_1).timeit(num_runs) / num_runs * 1000
    # day2_2_time = timeit.Timer(d2_2).timeit(num_runs) / num_runs * 1000
    # day3_1_time = timeit.Timer(d3_1).timeit(num_runs) / num_runs * 1000
    # day3_2_time = timeit.Timer(d3_2).timeit(num_runs) / num_runs * 1000
    # day4_1_time = timeit.Timer(d4_1).timeit(num_runs) / num_runs * 1000
    # day4_2_time = timeit.Timer(d4_2).timeit(num_runs) / num_runs * 1000
    # day5_1_time = timeit.Timer(d5_1).timeit(num_runs) / num_runs * 1000
    # day5_2_time = timeit.Timer(d5_2).timeit(num_runs) / num_runs * 1000
    day6_1_time = timeit.Timer(d6_1).timeit(num_runs) / num_runs * 1000
    day6_2_time = timeit.Timer(d6_2).timeit(num_runs) / num_runs * 1000

    pretty_print_table = \
        [
            ['part', 'result', f'avg (ms) / {num_runs} iter'],
            ['----------', '----------', '--------------------'],
            # ['day1_1', d1_1(), round(day1_1_time, 6)],
            # ['day1_2', d1_2(), round(day1_2_time, 6)],
            # ['day2_1', d2_1(), round(day2_1_time, 6)],
            # ['day2_2', d2_2(), round(day2_2_time, 6)],
            # ['day3_1', d3_1(), round(day3_1_time, 6)],
            # ['day3_2', d3_2(), round(day3_2_time, 6)],
            # ['day4_1', d4_1(), round(day4_1_time, 6)],
            # ['day4_2', d4_2(), round(day4_2_time, 6)],
            # ['day5_1', d5_1(), round(day5_1_time, 6)],
            # ['day5_2', d5_2(), round(day5_2_time, 6)],
            ['day6_1', d6_1(), round(day6_1_time, 6)],
            ['day6_2', d6_2(), round(day6_2_time, 6)],
        ]
    for row in pretty_print_table:
        print('| {:^10} | {:>10} | {:>20} |'.format(*row))
