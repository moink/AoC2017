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
    sum = 0
    data = [int(char) for char in advent_tools.read_whole_input()]
    jump = len(data)//2
    for first, second in zip(data, data[1:] + [data[0]]):
        # print(first, second)
        if first==second:
            sum = sum + first
    print(sum)


def run_part_2():
    sum = 0
    data = [int(char) for char in advent_tools.read_whole_input()]
    jump = len(data) // 2
    for first, second in zip(data, data[jump:] + data[:jump]):
        # print(first, second)
        if first == second:
            sum = sum + first
    print(sum)


if __name__ == '__main__':
    run_part_1()
    run_part_2()