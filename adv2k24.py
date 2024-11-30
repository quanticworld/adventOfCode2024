import timeit
from day1.code import part1 as d1_1
from day1.code import part2 as d1_2

if __name__ == '__main__':
    num_runs = 1
    day1_1_time = timeit.Timer(d1_1).timeit(num_runs) / num_runs * 1000
    day1_2_time = timeit.Timer(d1_2).timeit(num_runs) / num_runs * 1000

    pretty_print_table = \
        [
            ['part', 'result', f'avg (ms) / {num_runs} iter'],
            ['----------', '----------', '--------------------'],
            ['day1_1', d1_1(), round(day1_1_time, 6)],
            ['day1_2', d1_2(), round(day1_2_time, 6)],
        ]
    for row in pretty_print_table:
        print('| {:^10} | {:>10} | {:>20} |'.format(*row))
