import timeit
from day1.code import part1 as d1_1
from day1.code import part2 as d1_2
from day2.code import part1 as d2_1
from day2.code import part2 as d2_2
from day3.code import part1 as d3_1
from day3.code import part2 as d3_2

if __name__ == '__main__':
    num_runs = 10
    day1_1_time = timeit.Timer(d1_1).timeit(num_runs) / num_runs * 1000
    day1_2_time = timeit.Timer(d1_2).timeit(num_runs) / num_runs * 1000
    day2_1_time = timeit.Timer(d2_1).timeit(num_runs) / num_runs * 1000
    day2_2_time = timeit.Timer(d2_2).timeit(num_runs) / num_runs * 1000
    day3_1_time = timeit.Timer(d3_1).timeit(num_runs) / num_runs * 1000
    day3_2_time = timeit.Timer(d3_2).timeit(num_runs) / num_runs * 1000

    pretty_print_table = \
        [
            ['part', 'result', f'avg (ms) / {num_runs} iter'],
            ['----------', '----------', '--------------------'],
            ['day1_1', d1_1(), round(day1_1_time, 6)],
            ['day1_2', d1_2(), round(day1_2_time, 6)],
            ['day2_1', d2_1(), round(day2_1_time, 6)],
            ['day2_2', d2_2(), round(day2_2_time, 6)],
            ['day3_1', d3_1(), round(day3_1_time, 6)],
            ['day3_2', d3_2(), round(day3_2_time, 6)],
        ]
    for row in pretty_print_table:
        print('| {:^10} | {:>10} | {:>20} |'.format(*row))
