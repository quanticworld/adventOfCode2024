import functools
import itertools

# SPOILER ALERT - Le code est dégueu, vie de papa oblige, le week-end :)


def solve(operators):
    operations = [line.split(':') for line in open("day7/sample.txt", "r").read().splitlines()]
    operations = list(map(lambda row: (int(row[0]), row[1].strip()), operations))

    matches_found = dict()

    # Pré-calculer les combinaisons d'opérateurs
    op_combi_cache = {}
    for i in range(15):
        op_combi_cache[i] = list(itertools.product(operators, repeat=i))

    for op in operations:
        total, operands = op[0], op[1]
        operators_indices = [i for i, x in enumerate(operands) if x == ' ']
        for subset in op_combi_cache[len(operators_indices)]:
            if total in matches_found:
                break
            operation = operands
            op_pos = -1
            for idx in reversed(operators_indices):
                operation = f'{operation[:idx]}#{subset[op_pos]}{operation[idx + 1:]}'
                op_pos -= 1

            # Triplement dégueu - des eval() en pagaille, dans une boucle de l'enfer
            op_chunks = operation.split('#')
            result = functools.reduce(lambda op1, op2: eval(f'{op1}{op2}'), op_chunks)

            if result == total:
                matches_found[total] = True
                break

    return sum(matches_found.keys())


def part1():
    return solve(['+', '*'])


def part2():
    return solve(['+', '*', ''])
