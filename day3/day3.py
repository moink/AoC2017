import contextlib
import collections
import copy
import functools
import itertools
import math
import numpy as np
import pandas as pd
import re

import advent_tools


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
    cc = itertools.count()
    grid = np.zeros((100, 100))
    x = 0
    y = 0
    grid[x+50, y+50] = 1
    step = 1
    while True:
        for s in range(step):
            x = x + 1
            n = sum(
                grid[x + a, y + b] for a in [49, 50, 51] for b in [49, 50, 51])
            grid[x + 50, y + 50] = n
            if n >= my_input:
                return n
        for s in range(step):
            y = y + 1
            n = sum(
                grid[x + a, y + b] for a in [49, 50, 51] for b in [49, 50, 51])
            grid[x + 50, y + 50] = n
            if n >= my_input:
                return n
        for s in range(step + 1):
            x = x - 1
            n = sum(
                grid[x + a, y + b] for a in [49, 50, 51] for b in [49, 50, 51])
            grid[x + 50, y + 50] = n
            if n >= my_input:
                return n
        for s in range(step + 1):
            y = y - 1
            n = sum(
                grid[x + a, y + b] for a in [49, 50, 51] for b in [49, 50, 51])
            grid[x + 50, y + 50] = n
            if n >= my_input:
                return n
        step = step + 2


if __name__ == '__main__':
    # print(math.sqrt(368078))
    # print(run_part_1())
    print(run_part_2())