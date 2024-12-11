import timeit
from day1.code import part1 as d1_1, part2 as d1_2
from day2.code import part1 as d2_1, part2 as d2_2
from day3.code import part1 as d3_1, part2 as d3_2
from day4.code import part1 as d4_1, part2 as d4_2
from day5.code import part1 as d5_1, part2 as d5_2
from day6.code import part1 as d6_1, part2 as d6_2
from day7.code import part1 as d7_1, part2 as d7_2
from day8.code import part1 as d8_1, part2 as d8_2
from day9.code import part1 as d9_1, part2 as d9_2
from day10.code import part1 as d10_1, part2 as d10_2
from day11.code import part1 as d11_1, part2 as d11_2


if __name__ == '__main__':
    num_runs = 1
    #day1_1_time = timeit.Timer(d1_1).timeit(num_runs) / num_runs * 1000
    #day1_2_time = timeit.Timer(d1_2).timeit(num_runs) / num_runs * 1000
    #day2_1_time = timeit.Timer(d2_1).timeit(num_runs) / num_runs * 1000
    #day2_2_time = timeit.Timer(d2_2).timeit(num_runs) / num_runs * 1000
    #day3_1_time = timeit.Timer(d3_1).timeit(num_runs) / num_runs * 1000
    #day3_2_time = timeit.Timer(d3_2).timeit(num_runs) / num_runs * 1000
    #day4_1_time = timeit.Timer(d4_1).timeit(num_runs) / num_runs * 1000
    #day4_2_time = timeit.Timer(d4_2).timeit(num_runs) / num_runs * 1000
    #day5_1_time = timeit.Timer(d5_1).timeit(num_runs) / num_runs * 1000
    #day5_2_time = timeit.Timer(d5_2).timeit(num_runs) / num_runs * 1000
    #day6_1_time = timeit.Timer(d6_1).timeit(num_runs) / num_runs * 1000
    #day6_2_time = timeit.Timer(d6_2).timeit(num_runs) / num_runs * 1000
    #day7_1_time = timeit.Timer(d7_1).timeit(num_runs) / num_runs * 1000
    #day7_2_time = timeit.Timer(d7_2).timeit(num_runs) / num_runs * 1000
    #day8_1_time = timeit.Timer(d8_1).timeit(num_runs) / num_runs * 1000
    #day8_2_time = timeit.Timer(d8_2).timeit(num_runs) / num_runs * 1000
    #day9_1_time = timeit.Timer(d9_1).timeit(num_runs) / num_runs * 1000
    #day9_2_time = timeit.Timer(d9_2).timeit(num_runs) / num_runs * 1000
    #day10_1_time = timeit.Timer(d10_1).timeit(num_runs) / num_runs * 1000
    #day10_2_time = timeit.Timer(d10_2).timeit(num_runs) / num_runs * 1000
    day11_1_time = timeit.Timer(d11_1).timeit(num_runs) / num_runs * 1000
    day11_2_time = timeit.Timer(d11_2).timeit(num_runs) / num_runs * 1000

    pretty_print_table = \
        [
            ['part', 'result', f'avg (ms) / {num_runs} iter'],
            ['----------', '----------', '--------------------'],
            #['day1_1', d1_1(), round(day1_1_time, 6)],
            #['day1_2', d1_2(), round(day1_2_time, 6)],
            #['day2_1', d2_1(), round(day2_1_time, 6)],
            #['day2_2', d2_2(), round(day2_2_time, 6)],
            #['day3_1', d3_1(), round(day3_1_time, 6)],
            #['day3_2', d3_2(), round(day3_2_time, 6)],
            #['day4_1', d4_1(), round(day4_1_time, 6)],
            #['day4_2', d4_2(), round(day4_2_time, 6)],
            #['day5_1', d5_1(), round(day5_1_time, 6)],
            #['day5_2', d5_2(), round(day5_2_time, 6)],
            #['day6_1', d6_1(), round(day6_1_time, 6)],
            #['day6_2', d6_2(), round(day6_2_time, 6)],
            #['day7_1', d7_1(), round(day7_1_time, 6)],
            #['day7_2', d7_2(), round(day7_2_time, 6)],
            #['day8_1', d8_1(), round(day8_1_time, 6)],
            #['day8_2', d8_2(), round(day8_2_time, 6)],
            #['day9_1', d9_1(), round(day9_1_time, 6)],
            #['day9_2', d9_2(), round(day9_2_time, 6)],
            #['day10_1', d10_1(), round(day10_1_time, 6)],
            #['day10_2', d10_2(), round(day10_2_time, 6)],
            ['day11_1', d11_1(), round(day11_1_time, 6)],
            ['day11_2', d11_2(), round(day11_2_time, 6)],
        ]
    for row in pretty_print_table:
        print('| {:^10} | {:>10} | {:>20} |'.format(*row))
