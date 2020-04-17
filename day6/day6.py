import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re

import advent_tools


def run_part_1():
    seen = set()
    banks = [int(num) for num in advent_tools.read_whole_input().split()]
    # banks = [0, 2, 7, 0]
    count = 0
    while True:
        count = count + 1
        maxval = max(banks)
        ind = banks.index(maxval)
        banks[ind] = 0
        for m in range(maxval):
            add_index = (ind + m + 1) % len(banks)
            banks[add_index] = banks[add_index] + 1
        # print(banks)
        if tuple(banks) in seen:
            break
        seen.add(tuple(banks))
    print(count)

def run_part_2():
    banks = [0, 14, 13, 12, 11, 10, 8, 8, 6, 6, 5, 3, 3, 2, 1, 10]
    init_banks = [num for num in banks]
    count = 0
    while True:
        count = count + 1
        maxval = max(banks)
        ind = banks.index(maxval)
        banks[ind] = 0
        for m in range(maxval):
            add_index = (ind + m + 1) % len(banks)
            banks[add_index] = banks[add_index] + 1
        if all(first == second for first, second in zip(banks, init_banks)):
            break
    print(count)


if __name__ == '__main__':
    # run_part_1()
    run_part_2()