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

class ExpCoprocessor(advent_tools.Computer):

    operation = advent_tools.Computer.operation
    return_register = 'h'

    def __init__(self):
        super().__init__()
        self.mul_count = 0

    @operation('set')
    def set_register(self, reg_num, key_or_val):
        val = self.get_key_or_val(key_or_val)
        self.registers[reg_num] = val

    @operation('sub')
    def subtract_from_register(self, reg_num, key_or_val):
        val = self.get_key_or_val(key_or_val)
        self.registers[reg_num] = self.registers[reg_num] - val

    @operation('mul')
    def multiply_register(self, reg_num, key_or_val):
        val = self.get_key_or_val(key_or_val)
        self.registers[reg_num] = self.registers[reg_num] * val
        self.mul_count += 1

    @operation('jnz')
    def jump(self, key_or_val1, key_or_val2):
        val = self.get_key_or_val(key_or_val1)
        offset = self.get_key_or_val(key_or_val2)
        if val:
            self.instruction_pointer = self.instruction_pointer + offset - 1

def run_part_1():
    computer = ExpCoprocessor()
    computer.run_input_file()
    return computer.mul_count


def is_prime(number):
    highest = math.ceil(math.sqrt(number))
    for factor in range(2, highest + 1):
        if number % factor == 0:
            return False
    return True


def run_part_2():
    count = 0
    for b in range(108100, 125101, 17):
        if not is_prime(b):
            count = count + 1
    return count

if __name__ == '__main__':
    print(run_part_1())
    print(run_part_2())