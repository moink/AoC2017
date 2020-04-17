import itertools

import numpy as np


def run_part_1():
    my_input = 368078
    cc = itertools.count()
    x = 0
    y = 0
    step = 1
    count = 1
    while True:
        for s in range(step):
            x = x + 1
            count = count + 1
            if count == my_input:
                return abs(x) + abs(y)
        for s in range(step):
            y = y + 1
            count = count + 1
            if count == my_input:
                return abs(x) + abs(y)
        for s in range(step + 1):
            x = x - 1
            count = count + 1
            if count == my_input:
                return abs(x) + abs(y)
        for s in range(step + 1):
            y = y - 1
            count = count + 1
            if count == my_input:
                return abs(x) + abs(y)
        step = step + 2


def run_part_2():
    my_input = 368078
    grid = np.zeros((100, 100))
    x = 0
    y = 0
    grid[x+50, y+50] = 1
    step = 1
    while True:
        for s in range(step):
            x = x + 1
            val = sum_neighbours(grid, x, y)
            grid[x + 50, y + 50] = val
            if val >= my_input:
                return val
        for s in range(step):
            y = y + 1
            val = sum_neighbours(grid, x, y)
            grid[x + 50, y + 50] = val
            if val >= my_input:
                return val
        for s in range(step + 1):
            x = x - 1
            val = sum_neighbours(grid, x, y)
            grid[x + 50, y + 50] = val
            if val >= my_input:
                return val
        for s in range(step + 1):
            y = y - 1
            val = sum_neighbours(grid, x, y)
            grid[x + 50, y + 50] = val
            if val >= my_input:
                return val
        step = step + 2


def sum_neighbours(grid, x, y):
    n = sum(grid[x + a, y + b] for a in [49, 50, 51] for b in [49, 50, 51])
    return n


if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())