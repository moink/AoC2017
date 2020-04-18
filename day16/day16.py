import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re
from string import ascii_lowercase
import advent_tools


def run_part_1():
    instructions = advent_tools.read_whole_input().split(',')
    letters = list(ascii_lowercase[:16])
    # instructions = ['s1', 'x3/4', 'pe/b']
    # letters = list('abcde')/
    letters = do_dance(instructions, letters)
    return ''.join(letters)

@functools.lru_cache(None)
def do_dance(instructions, letters):
    instructions = instructions.split(',')
    letters = list(letters)
    for inst in instructions:
        oper = inst[0]
        rest = inst[1:]
        if oper == 's':
            num = int(rest)
            letters = letters[-num:] + letters[:-num]
        elif oper == 'x':
            num1, num2 = (int(num) for num in rest.split('/'))
            letters = swap(letters, num1, num2)
        else:
            num1, num2 = (letters.index(let) for let in rest.split('/'))
            letters = swap(letters, num1, num2)  # print(''.join(letters))
    return ''.join(letters)


def swap(letters, num1, num2):
    temp = letters[num1]
    letters[num1] = letters[num2]
    letters[num2] = temp
    return letters


def run_part_2():
    instructions = advent_tools.read_whole_input()
    letters = ascii_lowercase[:16]
    init_letters = letters
    period = False
    for i in range(1000000000):
        if i % 10000000 == 0:
            print(i)
        letters = do_dance(instructions, letters)
        if letters == init_letters and not period:
            period = True
            print('Period: ', i)
    return ''.join(letters)


if __name__ == '__main__':
    # print(run_part_1())
    print(run_part_2())