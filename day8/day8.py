import contextlib
import collections
import copy
import functools
import itertools
import numpy as np
import pandas as pd
import re

import advent_tools

class TheComputer(advent_tools.Computer):

    operation = advent_tools.Computer.operation
    return_register = 'y'

    def __init__(self):
        super().__init__()
        self.max_val = 2971

    def run_instruction(self, instruction):
        """Run a single instruction

        Using the first word of the instruction, figure out what operation
        to run. Pass the rest of the words of the instruction as an argument.

        Args:
            instruction: str
                Instruction to run. Must start with a valid operation
                identifier (key of self.operation_map)

        Returns:
            None
        """
        words = instruction.split()
        func = self.operation_map[words[1]]
        func(self, *([words[0]] + words[2:]))
        self.max_val = max(self.max_val, max(self.registers.values()))

    @operation('inc')
    def increase(self, name, amount, _, compare, oper, num):
        reg_val = self.registers[compare]
        if eval(str(reg_val) + oper + num):
            self.registers[name] = self.registers[name] + int(amount)

    @operation('dec')
    def decrease(self, name, amount, _, compare, oper, num):
        reg_val = self.registers[compare]
        rhs = int(num)
        if eval(str(reg_val) + oper + num):
            self.registers[name] = self.registers[name] - int(amount)

def run_both_parts():
    computer = TheComputer()
    computer.run_input_file()
    print('Part 1:', max(computer.registers.values()))
    print('Part 2:', computer.max_val)


if __name__ == '__main__':
    run_both_parts()
