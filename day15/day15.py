import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re

import advent_tools

def genA(start=512):
    for number in itertools.count(start=1):

        num = (start * pow(16807, number, 2147483647) % 2147483647) % 65536
        if num % 4 == 0:
            yield format(num, '016b')

def genB(start=191):
    for number in itertools.count(start=1):
        num = (start * pow(48271, number, 2147483647) % 2147483647) % 65536
        if num % 8 == 0:
            yield format(num, '016b')


def run_part_1():
    return calc_up_to_n(40000000)


def calc_up_to_n(n):
    return sum(genA(i) == genB(i) for i in range(1, n + 1))


def run_part_2():
    count = 0
    a = genA()
    b = genB()
    for i in range(5000000):
        if i % 10000 == 0:
            print(i)
        if next(a) == next(b):
            count = count + 1
    return count


if __name__ == '__main__':
    # print(run_part_1())
    print(run_part_2()) # 301 is too low