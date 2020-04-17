import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re

import advent_tools

def score(num, data):
    if '{' not in data:
        return num
    count = 1
    if data.startswith('{'):
        inside = ''
        for pos, char in enumerate(data[1:]):
            if char == '{':
                count = count + 1
            elif char == '}':
                count = count - 1
                if count == 0:
                    return score(num + 1, inside) + score(num, data[pos+1:])
            inside = inside + char
    else:
        return score(num, '{' + data.split('{', maxsplit=1)[1])
    return 0


def remove_garbage(data):
    count = 0
    in_angle = False
    result = ''
    for char in data:
        if in_angle:
            if char == '>':
                in_angle = False
            else:
                count = count + 1
        else:
            if char == '<':
                in_angle = True
            else:
                result = result + char
    return result, count

def clean_ex(data):
    while '!' in data:
        pos = data.index('!')
        data = data[:pos] + data[pos+2:]
    return data

def run_part_1():
    data = advent_tools.read_whole_input()
    # data = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
    data = clean_ex(data)
    data, count = remove_garbage(data)
    # print(score(0, data))
    # print(count)
    print(advent_tools.recursive_inside_outside(data, '{', '}'))
    #1325 is too low


def run_part_2():
    pass


if __name__ == '__main__':
    run_part_1()
    run_part_2()