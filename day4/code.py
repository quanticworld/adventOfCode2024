def count_occurrences(patterns, matrix):
    return sum(
        all(pattern[j][i] == ' ' or pattern[j][i] == matrix[y + j][x + i]
            for j in range(len(pattern)) for i in range(len(pattern[0]))
        )
        for pattern in patterns
        for y in range(len(matrix) - len(pattern) + 1)
        for x in range(len(matrix[0]) - len(pattern[0]) + 1)
    )

def part1():
    matrix = [line for line in open("day4/sample.txt", "r").read().splitlines()]
    return count_occurrences(patterns_part1, matrix)


def part2():
    matrix = [line for line in open("day4/sample.txt", "r").read().splitlines()]
    return count_occurrences(patterns_part2, matrix)

patterns_part1 = [['XMAS'],
            
            ['SAMX'],

            ['X', 
             'M', 
             'A', 
             'S'],

            ['S', 
             'A', 
             'M', 
             'X'],

            ['X   ',
             ' M  ',
             '  A ',
             '   S'],

            ['S   ',
             ' A  ',
             '  M ',
             '   X'],
            
            ['   X',
             '  M ',
             ' A  ',
             'S   '],

            ['   S',
             '  A ',
             ' M  ',
             'X   ']
             ]
            
patterns_part2 = [
    ['M S',
     ' A ',
     'M S'],

    ['S M',
     ' A ',
     'S M'],

    ['S S',
     ' A ',
     'M M'],

    ['M M',
     ' A ',
     'S S'],
]