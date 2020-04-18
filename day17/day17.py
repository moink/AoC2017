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
    stepsize = 301
    buffer = [0]
    curpos = 0
    for i in range (1, 2018):
        curpos = (curpos + stepsize) % len(buffer) + 1
        buffer.insert(curpos, i)
        # print(buffer)
    return(buffer[curpos + 1])


def run_part_2():
    stepsize = 301
    buffer_len = 1
    curpos = 0
    place1 = 0
    for i in range(1, 50000000):
        if i % 1000000 == 0:
            print(i)
        curpos = (curpos + stepsize) % buffer_len + 1
        buffer_len = buffer_len + 1
        if curpos == 1:
            place1 = i
    return place1

if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())