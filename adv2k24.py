import timeit
from importlib import import_module

if __name__ == '__main__':
    num_runs = 1
    results = []

    for day in range(1, 13):
        module = import_module(f"day{day}.code")
        for part in (1, 2):
            func = getattr(module, f"part{part}")
            avg_time = timeit.Timer(func).timeit(num_runs) / num_runs * 1000
            result = func()
            results.append([f"day{day}_{part}", result, round(avg_time, 6)])

    pretty_print_table = [["part", "result", f"avg (ms) / {num_runs} iter"]]
    pretty_print_table.append(["----------", "----------", "--------------------"])
    pretty_print_table.extend(results)

    for row in pretty_print_table:
        print('| {:^10} | {:>10} | {:>20} |'.format(*row))