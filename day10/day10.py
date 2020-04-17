import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re

from operator import xor

import advent_tools


def run_part_1():
    lengths = [int(num) for num in advent_tools.read_whole_input().split(',')]
    result, _, _ = run_operations(lengths, list(range(256)))
    return (result[0] * result[1])


def run_operations(lengths, result, current_pos=0, skip_size=0):
    for length in lengths:
        reslen = len(result)
        to_rev = []
        positions = []
        for r in range(length):
            pos = (current_pos + r) % reslen
            positions.append(pos)
            to_rev.append(result[pos])
        revd = list(reversed(to_rev))
        for pos, item in zip(positions, revd):
            result[pos] = item
        current_pos = current_pos + length + skip_size
        skip_size = skip_size + 1
    return result, current_pos, skip_size

def convert_ascii(chars):
    return [ord(char) for char in chars]

def run_part_2():
    lengths = (convert_ascii(advent_tools.read_whole_input())
               + [17, 31, 73, 47, 23])
    pos = 0
    skip = 0
    result = list(range(256))
    for i in range(64):
        result, pos, skip = run_operations(lengths, result, pos, skip)
    dense = []
    for chunk in advent_tools.chunk_iterable(result, 16):
        hexval = hex(functools.reduce(xor, chunk, 0))
        if len(hexval) == 4:
            dense.append(hexval[2:])
        else:
            dense.append('0' + hexval[2:])
    return ''.join(dense)


if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())
